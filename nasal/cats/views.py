from django.shortcuts import render,get_object_or_404
from cats.forms import AddCatComment
from homepage.views import detailed
from .models import Cat

popularCats = [
{
    'breedname':'SIAMESE',
    'description':'Popular since the 19th century, this cat breed originated in Thailand (formerly known as Siam). The Siamese has been a foundational breed for the Oriental shorthair, sphynx, and Himalayan. Most Siamese cats have distinct markings called "points" that are the areas of coloration on their face, ears, feet, and tail. Two varieties of Siamese cats have an "apple" shaped head and chubbier body and the other features a larger head and slender body. The animated Disney film "Lady and the Tramp" featured Siamese cats singing a song, demonstrating their intelligence and vocal skills. Many Siamese cats that originated from Thailand had a kink in their tail—a trait bred out of most Siamese, but you can still see it in street cats in Thailand.',
    'breed_image':'https://www.blogsmonitor.com/news/gallery/siamese-cats/siamese_cats_3.jpg',
},
{
    'breedname':'PERSIAN',
    'description':'Also lovingly referred to as one of the "smushed-face" cats, the Iranian cat or Shiraz cat (named for a city in Iran), Persians have beautiful, long fur coats. They can come in almost any color and have a flat face when compared to most other breeds of cats. Persians are featured in many movies, artworks, and commercials and have been one of the most popular breeds of cats for decades. Their coats demand regular grooming, otherwise, matting will result. Like many purebreds, they are prone to a variety of diseases, including renal and cardiac problems.',
    'breed_image':'http://bin3aiah.net/wp-content/uploads/2018/11/1280-633113756-white-persian-cats.jpg',
},
{
    'breedname':'MAINE COON',
    'description':'Known for its large stature and thick fur coat, the Maine coon is a cat that is difficult to ignore. Hailing from the state of Maine and the state’s official cat, the Maine coon is a gentle giant. They are great hunters and were popularized after the CFA recognized them as purebred in the late 1970s. They remain one of the most popular cat breeds. Many Maine coons have polydactylism, or extra toes, which makes their already large feet even larger. This great feature helps for hunting in the snow since large feet act as snowshoes. The classic Maine coon coloration is a brown tabby, but this breed can come in almost any color.',
    'breed_image':'http://3.bp.blogspot.com/-8gnCYUNbyZ8/UgVGyoIybFI/AAAAAAAAAQc/XN1WcvlAaPI/s1600/maine-coon-2.jpg',
},
{
    'breedname':'RAGDOLL',
    'description':'Ragdoll cats get their name from their docile temperament. They tend to go limp when picked up, much like a rag doll. At one time, people thought they couldn’t feel pain, but that is not true. Ragdolls look a lot like long-haired Siamese cats with pointed color patterns. They also have distinctive blue eyes and dog-like personalities, following their owners around the house.',
    'breed_image':'https://www.felineliving.net/wp-content/uploads/2018/01/ragdoll-kitty-e1522101384737.jpg',
},
{
    'breedname':'BENGAL',
    'description':'Bengals are wild-looking cats—literally. Their markings make them look more like they belong in the jungle rather than in your home, but they are domesticated. They are talkative and require a lot of exercise. They come in many colors with patterns like spots and rosettes. Their name comes from the Asian leopard cat’s taxonomic name, Prionailurus bengalensis bengalensis. Bengals were initially bred from domestic cats and a wildcat. They also get their beautiful patterns from this wildcat.',
    'breed_image':'https://upload.wikimedia.org/wikipedia/commons/5/5d/Bengal_cat1.jpg',
},
{
    'breedname':'ABYSSINIAN',
    'description':'Originally from Ethiopia (previously known as Abyssinia), the Abyssinian cat has a distinctive ruddy agouti coat that gives the Abyssinian its unique banded look. It has tall, pointy ears; a wedge-shaped head; and a slender and muscular body. Personality-wise, Abys are active, curious cats that frequently follow owners around. Their playful, dog-like demeanor endears them to their humans.',
    'breed_image':'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg',
},
{
    'breedname':'BIRMAN',
    'description':'Birmans are another color-pointed cat like the Siamese and ragdoll. They have blue eyes and a medium-long coat but no undercoat, the primary trait that sets them apart from Persians and Himalayans. Birmans were the original stock for breeding ragdolls, so they look very similar, but they have slightly different markings and personalities. They are fun, social cats that love attention—from their chosen person. They are more of a one-person cat than others.',
    'breed_image':'https://www.catster.com/wp-content/uploads/2015/06/1-600-sealpoint-birman.jpg',
},
{
    'breedname':'ORIENTAL SHORTHAIR',
    'description':'At a glance, you may think this slender cat looks like a Siamese, but the Oriental shorthair is a separate breed. Unlike Siamese cats, they usually have green eyes and many color patterns and colors. The Oriental can also have long hair. Oriental shorthair cats are prone to skin cancer and getting cold due to their lack of fur; they are often seen wearing sweaters.',
    'breed_image':'https://cdn0.wideopenpets.com/wp-content/uploads/2020/04/Untitled-design-2020-04-13T214423.485-770x405.jpg',
},
{
    'breedname':'SPHYNX',
    'description':'If you are looking for a cat that doesn\'t shed, then the sphynx is for you. Sphynx cats look unique due to their lack of fur and are very social, active, dog-like felines. They look like they belong in the laps of royalty, but they are playful and goofy and act more like court jesters despite their regal appearance.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/sphynx-574228.jpeg',
},
{
    'breedname':'DEVON REX',
    'description':'Devon rex cats have wavy, soft short hair and slender bodies with enormous ears. The Devon rex is a playful, active cat described as "a monkey in a catsuit." This kitty will steal your heart with its lively, sweet disposition. They are also trainable and adept at learning tricks.',
    'breed_image':'https://kittywise.com/wp-content/uploads/2019/03/Devon-Rex.jpeg',
},
]

fluffiestCats = [
{
    'breedname':'PERSIAN',
    'description':'Also lovingly referred to as one of the "smushed-face" cats, the Iranian cat or Shiraz cat (named for a city in Iran), Persians have beautiful, long fur coats. They can come in almost any color and have a flat face when compared to most other breeds of cats. Persians are featured in many movies, artworks, and commercials and have been one of the most popular breeds of cats for decades. Their coats demand regular grooming, otherwise, matting will result. Like many purebreds, they are prone to a variety of diseases, including renal and cardiac problems.',
    'breed_image':'http://bin3aiah.net/wp-content/uploads/2018/11/1280-633113756-white-persian-cats.jpg',
},
{
    'breedname':'MAINE COON',
    'description':'Known for its large stature and thick fur coat, the Maine coon is a cat that is difficult to ignore. Hailing from the state of Maine and the state’s official cat, the Maine coon is a gentle giant. They are great hunters and were popularized after the CFA recognized them as purebred in the late 1970s. They remain one of the most popular cat breeds. Many Maine coons have polydactylism, or extra toes, which makes their already large feet even larger. This great feature helps for hunting in the snow since large feet act as snowshoes. The classic Maine coon coloration is a brown tabby, but this breed can come in almost any color.',
    'breed_image':'http://3.bp.blogspot.com/-8gnCYUNbyZ8/UgVGyoIybFI/AAAAAAAAAQc/XN1WcvlAaPI/s1600/maine-coon-2.jpg',
},
{
    'breedname':'RAGDOLL',
    'description':'Ragdoll cats get their name from their docile temperament. They tend to go limp when picked up, much like a rag doll. At one time, people thought they couldn’t feel pain, but that is not true. Ragdolls look a lot like long-haired Siamese cats with pointed color patterns. They also have distinctive blue eyes and dog-like personalities, following their owners around the house.',
    'breed_image':'https://www.felineliving.net/wp-content/uploads/2018/01/ragdoll-kitty-e1522101384737.jpg',
},
{
    'breedname':'RAGAMUFFIN',
    'description':'Cousin to the Ragdoll, the Ragamuffin shares a lot of similarities with the breed. He is fluffy and has the same weekly brushing requirements. He also goes limp when relaxed, and some Ragamuffins can be trained with basic commands. He will follow you everywhere you go, and because he meets you at the door whenever you get home, it will feel like he sits and waits for you.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/ragamuffin-646514.jpeg',
},
{
    'breedname':'HIMALYAN',
    'description':'The Himalayan is a specific colorpoint of the Persian and is more properly referred to as the Himalayan Persian by some cat registries. However, he was created by crossing the Persian with the Siamese, which gives him the furry coat of the Persian but the coloring of the Siamese. He can be considered lazy and he needs the same daily brushing as his Persian cousin. He will love his family but may not have as much time for strangers.',
    'breed_image':'https://www.catster.com/wp-content/uploads/2019/11/Himalayan_HI_Yamazaki.png',
},
{
    'breedname':'SOMALI',
    'description':'The Somali is a close relative to the short-haired Abyssinian. He has the same muscular, athletic physique, but he has a long, furry coat. He requires plenty of exercise and does shed quite a lot, but he does not require daily brushing. In fact, a weekly brush should prove ample to get rid of knots and to remove dead hairs. The Somali is a very sociable cat that will get on with everybody, whether they’re family or passing strangers.',
    'breed_image':'https://petsfeed.co/wp-content/uploads/2020/02/Somali-cat-02-863x1024.jpg',
},
{
    'breedname':'BIRMAN',
    'description':'Birmans are another color-pointed cat like the Siamese and ragdoll. They have blue eyes and a medium-long coat but no undercoat, the primary trait that sets them apart from Persians and Himalayans. Birmans were the original stock for breeding ragdolls, so they look very similar, but they have slightly different markings and personalities. They are fun, social cats that love attention—from their chosen person. They are more of a one-person cat than others.',
    'breed_image':'https://www.catster.com/wp-content/uploads/2015/06/1-600-sealpoint-birman.jpg',
},
{
    'breedname':'SIBERIAN',
    'description':'The Siberian has a thick, double coat. This would have been used to protect the breed from freezing cold Siberian conditions, and he can still survive cold conditions today, although he would much rather be sat indoors on your lap. He is a very intelligent cat, gets on with all members of the family, even canines, and he sheds a lot less than some other long-haired fluffy breeds. For most of the year, the Siberian requires only weekly brushing, but during shedding season he will need daily brushing to remove the clumps of fur.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/siberian-582073.png',
},
{
    'breedname':'NORWEGIAN FOREST CAT',
    'description':'The Norwegian Forest Cat is the official cat of Norway. He is a muscular cat with moderate energy levels and is child-friendly, dog-friendly, adult-friendly, and stranger friendly. He does prefer to be up high, so you should consider investing in a climbing tree, and be prepared to look for him on top of cupboards and inside your Christmas tree. In terms of grooming, be prepared to brush once or twice a week.',
    'breed_image':'http://www.catloversdiary.com/wp-content/uploads/2013/04/Norwegian_Forest_Cat.jpg',
},
]
dangerousCats =[
{
    'breedname':'BOBCAT',
    'description':'Bobcat is considered by far the most dangerous domestic cat breeds in the world. The cat breed resides majorly in parts of southern Canada, central Mexico, and United States. The Bobcats are known to be sturdy by looks and another mid-sized Lynx. Additionally, the cat is known to be very aggressive and can hurt an adult human to a greater extent. Further, the cat breed is most active at night and are confined within its defined territories. The bobcats are very intelligent in stalking their prey and possess an incredible hunting skill. They often prey on rabbits and other rodents. Furthermore, they are known to survive for long without food.',
    'breed_image':'https://i2.wp.com/www.tbreporter.com/wp-content/uploads/2016/08/bobcat-release-4.jpg?fit=984%2C984&ssl=1',
},
{
    'breedname':'MAINE COON',
    'description':'Maine Coon is yet another dangerous cat to own as a pet at home. The cat breed is considered the largest domestic cat breed in the world. The cat breed is also recognized as “the gentle giant” and is characterized by a robust body and bone structure. The dangers imposed by them are classified based on the stranger’s behavior. Additionally, the Maine Coons are friendly with their owner and are known to be jovial throughout their life. They are native to Maine, United States. Finally, the cat breed is known to replicate the exact same characteristics of a dog.',
    'breed_image':'https://image.freepik.com/free-photo/aggressive-maine-coon-cat_87557-12935.jpg',
},
{
    'breedname':'MANUL',
    'description':'Manul cat breed is also famously recognized as “Pallas’s cat”. The cat breed is a comparatively small wild cat and resides majorly in the parts of Central Asia. Additionally, the cat is listed in the IUCN Red List of IUCN as Near Threatened species. The Pallas’s cats are experts in ambush and stalking. Further, they are one such cat breed who love to sit solitary throughout the day. Furthermore, they spend most of their day in burrows and caves and begin hunting at night. Finally, one should think twice before investing in Pallas’s cat.',
    'breed_image':'https://www.awesomeinventions.com/wp-content/uploads/2015/06/manul-scary.jpg',
},
{
    'breedname':'SERVAL',
    'description':'Serval is a dangerous wild cat that is native to Africa. The cat is medium-sized and can stand up to 62 cm in height. The servals are known to execute their prey in a very lethal manner. While they are in their hunt, they can be seen jumping and leaping up to a height of 2 m. Further, servals are known to produce a single-pounce-kill strategy. Additionally, their migration moto is very different and walk 2 to 4 kilometers every night. Furthermore, the cat can be seen as additional activities during cool and rainy environments.',
    'breed_image':'https://www.zoologiste.com/images/main/serval.jpg',
},
{
    'breedname':'SAVANNAH',
    'description':'Savannah is a savage and hybrid cat breed. The Savannahs are considered the largest cat breeds in the world. Additionally, the cat breed is a cross between a serval and a domestic cat. Further, the cat is known to produce incredible hunting skills. Also, a point to note that the cat has been banned by the Australian Federal government. Furthermore, as per the government of Australia, the cat breed could potentially threaten other native wildlife species. But, the other side of the character also accounts for some positivity. They are known to be social and friendly if they are well-trained by their owners.',
    'breed_image':'https://images.squarespace-cdn.com/content/53adb125e4b094aac18a8ee7/1471238968400-8ON6NTPDD191UDXF4J7M/F1hybridsSavannahs-August+14%2C+2016-13.jpg?content-type=image%2Fjpeg',
},
{
    'breedname':'OCELOT',
    'description':'Ocelot is a ferocious cat breed native to the southwestern United States, Mexico, and Central and South America. The body of ocelot is simply solid. The ocelots can consist of body-color with markings like a leopard. Additionally, the black markings, solid yellowish, tawny along with brownish background color produces a majestic look. Their hunting skills are incredible and are known to be more active at night. Further, the ocelots are known to even hunt down a deer for their meal. Their jaws are as much comparable to that of a Pitbull’s jaw.',
    'breed_image':'https://3.bp.blogspot.com/-sa1750lmTOg/WgapjNbHD8I/AAAAAAAAD5o/UIVkg4cMDDoyvZnmDSz_2M8FhREXzvuDwCLcBGAs/s1600/1_14_Ocelot.jpg',
},
{
    'breedname':'CHAUSIE CAT',
    'description':'Chausie cat is considered a domestic cat but the gene comes through a cross from a non-domestic jungle cat. The cat breed is medium in size and can be comparable to traditional domestic cats. Additionally, the cat’s fur can be color between grey and complete black. The vibrant body coloration can make then stand unique from other cat breeds across the globe. Further, the cat is very active and intelligent. Chausie cats are known to be social enough with dogs and humans. But they seem to find themselves difficult adjusting if re-homed as adults.',
    'breed_image':'https://upload.wikimedia.org/wikipedia/commons/0/06/ChausieA.jpg',
},
{
    'breedname':'JUNGLE CAT',
    'description':'The jungle cat is native to the Middle East, South and Southeast Asia, and southern China. The jungle cats are mid-sized and are also recognized as “swamp cat”. Further, they are uniformly sandy in color throughout its body. They are known to stay solo for the whole of its life except during the mating season. Additionally, they have exceptional hunting skills and are known to hunt throughout the day. Jungle cats hunt their prey by chasing and stalking. Furthermore, they are known to sprit up to a speed of 32 km/h and can swim up to 1.5 km in water to catch its prey.',
    'breed_image':'https://bigcatsindia.com/wp-content/uploads/2020/02/Jungle-Cat-Wild-Cat-1024x1009.jpg',
},
{
    'breedname':'BENGAL CAT',
    'description':'Bengal cat is a hybrid domestic cat breed originated from the United States. The cat breed resembles a Leopard as their ancestry of streams come from Leopard Cat. The marble-like pattern on the cat along with the spot is simply fantastic. Bengal cats are restricted by law in the cities of the United States. Additionally, there are strict rules and legalities in owning the cat breed in New York City, the state of Hawaii, Seattle, Washington, and Denver. Furthermore, the cat is known to be restricted and has complex rules and regulations to process ownership in the United Kingdom and Australia.',
    'breed_image':'https://pulpbits.net/wp-content/uploads/2014/01/bengal-cat-domestic.jpg',
},
{
    'breedname':'SIAMESE',
    'description':'Siamese is a Chinese cat breed, which was one of the most popular cat breeds in Europe and North America in the 19th Century. The cat’s fur coloration can range between chocolate paint, blue or pure white. The eyes are basically blue in color with distinctive short hair on the body. Siamese can be trained to be friendly and social with people. Additionally, they are intelligent by nature and are known to have dog-like characteristics.',
    'breed_image':'https://media.istockphoto.com/photos/siamese-cat-with-an-arched-back-and-growling-picture-id473084995?k=6&m=473084995&s=612x612&w=0&h=HT6PsSDy1grCw_78NBcS7-zbThlnKX0759_KAa6xjHE=',
},]

largestCats = [
{
    'breedname':'MAINE COON',
    'description':'Maine Coon is yet another dangerous cat to own as a pet at home. The cat breed is considered the largest domestic cat breed in the world. The cat breed is also recognized as “the gentle giant” and is characterized by a robust body and bone structure. The dangers imposed by them are classified based on the stranger’s behavior. Additionally, the Maine Coons are friendly with their owner and are known to be jovial throughout their life. They are native to Maine, United States. Finally, the cat breed is known to replicate the exact same characteristics of a dog.',
    'breed_image':'https://image.freepik.com/free-photo/aggressive-maine-coon-cat_87557-12935.jpg',
},
{
    'breedname':'SAVANNAH',
    'description':'Savannah is a savage and hybrid cat breed. The Savannahs are considered the largest cat breeds in the world. Additionally, the cat breed is a cross between a serval and a domestic cat. Further, the cat is known to produce incredible hunting skills. Also, a point to note that the cat has been banned by the Australian Federal government. Furthermore, as per the government of Australia, the cat breed could potentially threaten other native wildlife species. But, the other side of the character also accounts for some positivity. They are known to be social and friendly if they are well-trained by their owners.',
    'breed_image':'https://images.squarespace-cdn.com/content/53adb125e4b094aac18a8ee7/1471238968400-8ON6NTPDD191UDXF4J7M/F1hybridsSavannahs-August+14%2C+2016-13.jpg?content-type=image%2Fjpeg',
},
{
    'breedname':'NORWEGIAN FOREST CAT',
    'description':'The Norwegian Forest Cat is the official cat of Norway. He is a muscular cat with moderate energy levels and is child-friendly, dog-friendly, adult-friendly, and stranger friendly. He does prefer to be up high, so you should consider investing in a climbing tree, and be prepared to look for him on top of cupboards and inside your Christmas tree. In terms of grooming, be prepared to brush once or twice a week.',
    'breed_image':'http://www.catloversdiary.com/wp-content/uploads/2013/04/Norwegian_Forest_Cat.jpg',
},
{
    'breedname':'SIBERIAN',
    'description':'The Siberian has a thick, double coat. This would have been used to protect the breed from freezing cold Siberian conditions, and he can still survive cold conditions today, although he would much rather be sat indoors on your lap. He is a very intelligent cat, gets on with all members of the family, even canines, and he sheds a lot less than some other long-haired fluffy breeds. For most of the year, the Siberian requires only weekly brushing, but during shedding season he will need daily brushing to remove the clumps of fur.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/siberian-582073.png',
},
{
    'breedname':'RAGDOLL',
    'description':'Ragdoll cats get their name from their docile temperament. They tend to go limp when picked up, much like a rag doll. At one time, people thought they couldn’t feel pain, but that is not true. Ragdolls look a lot like long-haired Siamese cats with pointed color patterns. They also have distinctive blue eyes and dog-like personalities, following their owners around the house.',
    'breed_image':'https://www.felineliving.net/wp-content/uploads/2018/01/ragdoll-kitty-e1522101384737.jpg',
},
{
    'breedname':'RAGAMUFFIN',
    'description':'Cousin to the Ragdoll, the Ragamuffin shares a lot of similarities with the breed. He is fluffy and has the same weekly brushing requirements. He also goes limp when relaxed, and some Ragamuffins can be trained with basic commands. He will follow you everywhere you go, and because he meets you at the door whenever you get home, it will feel like he sits and waits for you.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/ragamuffin-646514.jpeg',
},
{
    'breedname':'CHAUSIE CAT',
    'description':'Chausie cat is considered a domestic cat but the gene comes through a cross from a non-domestic jungle cat. The cat breed is medium in size and can be comparable to traditional domestic cats. Additionally, the cat’s fur can be color between grey and complete black. The vibrant body coloration can make then stand unique from other cat breeds across the globe. Further, the cat is very active and intelligent. Chausie cats are known to be social enough with dogs and humans. But they seem to find themselves difficult adjusting if re-homed as adults.',
    'breed_image':'https://upload.wikimedia.org/wikipedia/commons/0/06/ChausieA.jpg',
},
]
beautifulCats =[
{
    'breedname':'ABYSSINIAN',
    'description':'Originally from Ethiopia (previously known as Abyssinia), the Abyssinian cat has a distinctive ruddy agouti coat that gives the Abyssinian its unique banded look. It has tall, pointy ears; a wedge-shaped head; and a slender and muscular body. Personality-wise, Abys are active, curious cats that frequently follow owners around. Their playful, dog-like demeanor endears them to their humans.',
    'breed_image':'https://upload.wikimedia.org/wikipedia/commons/9/9b/Gustav_chocolate.jpg',
},
{
    'breedname':'BIRMAN',
    'description':'Birmans are another color-pointed cat like the Siamese and ragdoll. They have blue eyes and a medium-long coat but no undercoat, the primary trait that sets them apart from Persians and Himalayans. Birmans were the original stock for breeding ragdolls, so they look very similar, but they have slightly different markings and personalities. They are fun, social cats that love attention—from their chosen person. They are more of a one-person cat than others.',
    'breed_image':'https://www.catster.com/wp-content/uploads/2015/06/1-600-sealpoint-birman.jpg',
},
{
    'breedname':'BENGAL CAT',
    'description':'Bengal cat is a hybrid domestic cat breed originated from the United States. The cat breed resembles a Leopard as their ancestry of streams come from Leopard Cat. The marble-like pattern on the cat along with the spot is simply fantastic. Bengal cats are restricted by law in the cities of the United States. Additionally, there are strict rules and legalities in owning the cat breed in New York City, the state of Hawaii, Seattle, Washington, and Denver. Furthermore, the cat is known to be restricted and has complex rules and regulations to process ownership in the United Kingdom and Australia.',
    'breed_image':'https://pulpbits.net/wp-content/uploads/2014/01/bengal-cat-domestic.jpg',
},
{
    'breedname':'HIMALYAN',
    'description':'The Himalayan is a specific colorpoint of the Persian and is more properly referred to as the Himalayan Persian by some cat registries. However, he was created by crossing the Persian with the Siamese, which gives him the furry coat of the Persian but the coloring of the Siamese. He can be considered lazy and he needs the same daily brushing as his Persian cousin. He will love his family but may not have as much time for strangers.',
    'breed_image':'https://www.catster.com/wp-content/uploads/2019/11/Himalayan_HI_Yamazaki.png',
},
{
    'breedname':'MAINE COON',
    'description':'Maine Coon is yet another dangerous cat to own as a pet at home. The cat breed is considered the largest domestic cat breed in the world. The cat breed is also recognized as “the gentle giant” and is characterized by a robust body and bone structure. The dangers imposed by them are classified based on the stranger’s behavior. Additionally, the Maine Coons are friendly with their owner and are known to be jovial throughout their life. They are native to Maine, United States. Finally, the cat breed is known to replicate the exact same characteristics of a dog.',
    'breed_image':'https://image.freepik.com/free-photo/aggressive-maine-coon-cat_87557-12935.jpg',
},
{
    'breedname':'PERSIAN',
    'description':'Also lovingly referred to as one of the "smushed-face" cats, the Iranian cat or Shiraz cat (named for a city in Iran), Persians have beautiful, long fur coats. They can come in almost any color and have a flat face when compared to most other breeds of cats. Persians are featured in many movies, artworks, and commercials and have been one of the most popular breeds of cats for decades. Their coats demand regular grooming, otherwise, matting will result. Like many purebreds, they are prone to a variety of diseases, including renal and cardiac problems.',
    'breed_image':'http://bin3aiah.net/wp-content/uploads/2018/11/1280-633113756-white-persian-cats.jpg',
},
{
    'breedname':'RAGAMUFFIN',
    'description':'Cousin to the Ragdoll, the Ragamuffin shares a lot of similarities with the breed. He is fluffy and has the same weekly brushing requirements. He also goes limp when relaxed, and some Ragamuffins can be trained with basic commands. He will follow you everywhere you go, and because he meets you at the door whenever you get home, it will feel like he sits and waits for you.',
    'breed_image':'https://cdn.fotofits.com/petzlover/gallery/img/l/ragamuffin-646514.jpeg',
},
{
    'breedname':'RAGDOLL',
    'description':'Ragdoll cats get their name from their docile temperament. They tend to go limp when picked up, much like a rag doll. At one time, people thought they couldn’t feel pain, but that is not true. Ragdolls look a lot like long-haired Siamese cats with pointed color patterns. They also have distinctive blue eyes and dog-like personalities, following their owners around the house.',
    'breed_image':'https://www.felineliving.net/wp-content/uploads/2018/01/ragdoll-kitty-e1522101384737.jpg',
},
{
    'breedname':'SIAMESE',
    'description':'Siamese is a Chinese cat breed, which was one of the most popular cat breeds in Europe and North America in the 19th Century. The cat’s fur coloration can range between chocolate paint, blue or pure white. The eyes are basically blue in color with distinctive short hair on the body. Siamese can be trained to be friendly and social with people. Additionally, they are intelligent by nature and are known to have dog-like characteristics.',
    'breed_image':'https://media.istockphoto.com/photos/siamese-cat-with-an-arched-back-and-growling-picture-id473084995?k=6&m=473084995&s=612x612&w=0&h=HT6PsSDy1grCw_78NBcS7-zbThlnKX0759_KAa6xjHE=',
},
]



# Create your views here.


def addcomment(request,id):
    form = AddCatComment()

    if request.method == 'POST':
        form = AddCatComment(request.POST)

        if form.is_valid():
            form.instance.cat_id = id
            form.save(commit=True)
            return render(request,'homepage/index.html')

    return render(request,'cats/cat_comment_section.html',{'form':form})




def largestcats(request):
    context = {'largestCats':largestCats}
    return render(request,'cats/largestcats.html',context)

def fluffiestcats(request):
    context = {'fluffiestCats':fluffiestCats}
    return render(request,'cats/fluffiestcats.html',context)

def popularcats(request):
    context = {'popularCats':popularCats}
    return render(request,'cats/popularcats.html',context)

def dangerouscats(request):
    context = {'dangerousCats':dangerousCats}
    return render(request,'cats/dangerouscats.html',context)

def beautifulcats(request):
    context = {'beautifulCats':beautifulCats}
    return render(request,'cats/beautifulcats.html',context)