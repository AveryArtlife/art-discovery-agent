#!/usr/bin/env python3
"""
Generate a comprehensive single-word list for .ai domain checking.
Uses NLTK's English word corpus plus curated tech/business terms.
"""

import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

# NLTK English words
word_list = words.words()
single_words = set(w.lower() for w in word_list if w.isalpha() and len(w) >= 1)

# Add single letters
for c in 'abcdefghijklmnopqrstuvwxyz':
    single_words.add(c)

# Add common tech, business, and brandable terms not in NLTK
extra = """
ai api app arc art auto base bit bot box bug buy cab cam cap car cat chat chip cli
cloud code coin cool core crm cto cyber dao dash data deep demo dev dig dna dns doc
dot ego elk elm end eng era erp eth eve fab fam fan faq fax fed fin fit fix fly fog
fun gab gal gap gas gem gen geo gig gin git gnu god gpu gum gun gut gym hack hat hex
hip hit hog hop hot hub hue hum ice icy ink inn ion iot ipo ivy jab jam jar jaw jay
jet jig job jog joy jug lab lad lag lap law lax lay led leg let lid lip lit log lot
low lux mac mad map max med meg men met mid min mix mob mod mom mop mud mug nap nav
net new nft nil nip nit nod nor not now npm nun nut oak oar oat odd ode oil old one
opt orb ore our out ova owe owl own pad pal pan paw pay pea peg pen per pet phi pie
pig pin pit ply pod pop pot pow pro pub pug pun pup put rad rag ram ran rap rat raw
ray red ref rep rev rib rid rig rim rip rob rod roe rot row rub rug rum run rut sag
sap sat saw say sea set sew she shy sim sin sip sir sit six ski sky sly sod sol son
sop sot sow soy spa spy sql sri sub sue sum sun sup tab tad tag tan tap tar tax tea
ten the tie tin tip toe ton too top tow toy try tub tug two uri url urn use van vat
vet via vie vim vip vow vue wad wag war was wax way web wed wet who why wig win wit
woe wok won woo wow yak yam yap yaw yea yen yes yet yew yin you zap zen zip zoo
zoom pixel nexus pulse spark quest forge vault prime swift blade storm dream flame
crown ridge steel titan omega alpha delta gamma sigma theta orbit lunar solar astro
cyber hyper ultra mega giga tera nano micro macro meta para proto retro turbo nitro
aero aqua pyro cryo flux wave beam glow drift shift sync link mesh node edge grid
loop stack cache queue hash token proxy relay route patch build craft blend morph
scale scope trace track trail trend proof trust valid smart sharp agile rapid bold
vivid lucid crisp sleek slick elite noble royal grand chief apex peak summit zenith
crest beacon signal flare echo sonic audio voice sound music render canvas sketch
paint brush color shade bloom lotus flora fauna coral amber ivory onyx jade ruby
pearl crystal prism lens optic vision sight focus clarity insight wisdom sage oracle
mystic enigma cipher rune glyph totem charm amulet relic essence spirit aura karma
mana chi nirvana utopia eden haven temple realm kingdom empire dynasty legacy epoch
genesis dawn dusk twilight aurora cosmos nebula galaxy quasar pulsar nova comet
meteor planet star moon earth terra atlas phoenix dragon griffin hydra sphinx falcon
eagle hawk raven wolf lion tiger bear panther jaguar cobra viper python mantis
firefly monarch osprey condor mercury venus mars jupiter saturn neptune pluto iris
hermes apollo athena artemis zeus hera eros nike muse fate fury grace hope faith
valor honor glory triumph victory champion hero legend myth saga epic archive studio
gallery arena plaza forum bazaar market guild alliance league order council depot
forge factory matrix helix spiral fractal quantum photon neutron proton electron
atom molecule polymer catalyst enzyme genome cortex neuron synapse nucleus plasma
fusion reactor dynamo turbine piston lever gear circuit transistor laser radar sonar
lidar fiber cable conduit pipeline channel tunnel bridge gateway portal vertex vortex
horizon compass vector tensor scalar array index cursor pointer buffer stream socket
packet frame block sector cluster shard replica mirror clone fork branch merge delta
commit deploy launch ignite kindle ember torch lantern prism quartz diamond sapphire
emerald garnet topaz opal agate marble granite basalt obsidian cobalt bronze copper
silver gold platinum titanium carbon silicon lithium helium neon argon iron zinc
nickel chrome steel alloy anvil hammer blade sword arrow shield banner badge crown
castle tower dome arch pillar vault terrace garden grove meadow field prairie jungle
forest glen dale gorge canyon cliff ridge mesa summit island reef lagoon bay cove
fjord marsh glacier breeze zephyr current tide surge ripple spiral helix coil thread
strand fiber silk velvet linen cotton wool canvas leather gleam shimmer sparkle
radiance glow blaze flash bolt spark flame ember ash mist fog vapor steam cloud
rainbow spectrum pulse beat rhythm tempo verse sonnet haiku ballad hymn anthem
chorus symphony waltz tango jazz blues funk soul reggae punk indie ambient techno
trance house disco opera ballet debut gala carnival festival sprint relay vault
archery fencing boxing judo karate rugby hockey polo golf tennis surfing diving
sailing kayak yacht fleet convoy squad patrol scout ranger sentinel warden marshal
captain admiral ace maverick rogue rebel pirate viking samurai ninja knight paladin
monk wizard bard herald scribe scholar mentor guru maven savant prodigy genius
maestro artisan smith mason potter weaver tailor baker brewer chef farmer hunter
miner pilot sailor explorer voyager pioneer founder architect builder maker creator
inventor designer planner strategist analyst advisor consul envoy delegate judge
advocate banker broker trader merchant tycoon mogul baron duke prince king queen
regent sovereign hamlet village colony frontier passage corridor arcade boulevard
avenue lane path route circuit milestone landmark monument antique vintage classic
modern novel fresh clean pure clear bright fierce brave loyal true fair kind warm
cool calm serene tranquil quiet subtle refined elegant pristine supreme infinite
eternal timeless enduring solid strong mighty robust resilient durable tough wild
primal organic vital crucial pivotal abundant unique rare singular remarkable
exceptional superb magnificent splendid majestic regal divine celestial ethereal
magical enchanting captivating mesmerizing electric dynamic vibrant legendary iconic
definitive resolute relentless persistent tenacious steadfast invincible
"""

for word in extra.split():
    word = word.strip().lower()
    if word.isalpha():
        single_words.add(word)

all_words = sorted(single_words)
with open("wordlist.txt", "w") as f:
    for w in all_words:
        f.write(w + "\n")

print(f"Generated wordlist.txt with {len(all_words)} unique words")
print(f"Breakdown by max length:")
for n in [1, 2, 3, 4, 5, 6, 7, 8, 10, 15]:
    count = len([w for w in all_words if len(w) <= n])
    print(f"  <= {n} chars: {count:>7,} words ({count:>7,} .ai domains)")
