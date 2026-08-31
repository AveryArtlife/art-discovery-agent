# Inbound inquiry audit: method

Reusable method for auditing gallery inbound inquiries across Artsy, Artnet and the
website contact form when all three deliver into one Gmail mailbox.

Contains no client data. Audit output itself is PII bearing and is never committed
to this repository, which is public. See `.gitignore`.

## The problem with Gmail threadId

A reply does not reliably share a thread with the inquiry it answers.

Observed failure modes:

- A colleague replying directly to the client while CC'ing the shared addresses
  creates a brand new thread with the same subject.
- Platform notification emails break threading on their own, so even a first party
  reply can land in a separate thread.

Measured on a 14 day window: roughly 20 of 21 answered inquiries would have been
scored "unanswered" if threadId had been trusted. Acting on that would mean sending
duplicate replies to clients who were already handled, which is the worst available
outcome for an inbound sales audit.

## The join key that works

Artsy issues a unique per-inquiry reply token as the notification's From address:

    <prefix>-<32 hex chars>@reply.artsy.net

Every outbound reply is addressed TO that token. The token is therefore an exact
foreign key between inquiry and reply, and it survives thread breaks.

Procedure:

1. Collect all inquiry notifications in the window, keyed by token.
2. Collect the complete Sent set for the window, plus all messages from colleagues
   whose replies CC the shared addresses.
3. Join on token, not threadId, not subject.
4. Fall back to normalized subject plus participant overlap only where no token
   exists, which is the case for direct email and website form inquiries.

## Known gap in the token join

A reply can answer an inquiry it is not addressed to. One observed case: a colleague
answered a second inquiry inside a message sent to the first inquiry's token
("I saw that you also inquired on ..."). A pure token join scores the second
inquiry as unanswered.

Mitigation: for any contact with more than one open inquiry, read the body of every
reply sent to that contact in the window before scoring.

## Three states, not two

Absence of a CC'd reply is weak evidence, not proof, because platform replies sent
inside the partner inbox generate no email at all.

- ANSWERED: reply visible in the mailbox.
- UNANSWERED, HIGH CONFIDENCE: no reply visible and no channel exists that could
  hide one. In practice this means direct email only.
- UNANSWERED, UNCONFIRMED: no reply visible but a platform inbox could hold one.

Every platform inquiry defaults to UNCONFIRMED. Since that collapses the majority
of rows into one bucket, subdivide by evidence strength so the list stays actionable:

1. Live conversation dropped: the contact wrote again and got nothing.
2. Same contact answered on a parallel inquiry in the window: highest duplicate
   reply risk, clear these first.
3. Platform default: no signal either way.

## Channel health checks worth running every time

These are findings about the pipeline, not about any single inquiry, and they bound
what the audit can see at all.

- Count inquiry notifications per platform. A paid channel producing zero inbound
  over a full window is a routing fault, not a quiet fortnight. Confirm membership
  status separately before concluding the channel is simply slow.
- Confirm website form submissions actually land in the audited mailbox. If only
  outbound replies are present, the originals deliver elsewhere and unanswered form
  inquiries are structurally invisible.
- Check whether platform replies are being sent inside the partner inbox. If they
  are, no email convention can catch them, and the fix is a workflow rule that all
  replies go out by email.

## Ranking

Sort by expected value, not date. Inputs, in rough order of weight:

- Platform buyer signals: confirmed buyer, ID verified, prior purchase count,
  "demonstrated budget in line with this artwork".
- Question depth. Shipping, condition and provenance questions are late funnel.
  An inquiry that skips price often means price is already acceptable.
- Multiple works from one contact, or multiple contacts on one work.
- Explicit follow up from the contact.
- Days elapsed, as a tiebreak rather than a primary sort.

Group by contact, not by work. One reply per person, not one per inquiry.
