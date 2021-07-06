from django.shortcuts import render
from cows.models import Cattle
from cows.forms import AddCattleComment

#Dictionaries
dairyCows = [
    {
        'breedname':'Holstein Friesian',
        'description':'This breed is considered to be the best milk producer of the world and widely distributed in most countries of the world. Under tropical conditions, they may not perform well, since they are the least heat tolerant, but crossbred cows have yielded more than 46 litres of milk a day.',
        'breed_image':'https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/1-a-holstein-friesian-cow-in-the-green-field-isa-fernandez.jpg',
    },
    {
        'breedname':'Jersey',
        'description':'Although the milk yield is not high, the breed is popular all over the world. There are some reasons for popularity which include a high percentage of butter fats (5.3%) in the milk and compare to other breeds. Early maturity of heifers produces calf between 26-30 months and has a regular calving interval, after that 12 – 13 months. A good herd produces average about 4500 liters of milk in 300 days lactation period.',
        'breed_image':'https://cdn.britannica.com/22/522-050-25222A61/Jersey-cow.jpg',
    },
    {
        'breedname':'Ayrshire',
        'description':'The milk of Ayrshire breed contains an average of 4% fat. Though the milk quality is better than the Holstein, its lower potential yield has resulted in the Ayrshire being replaced by Holstein. However, the champion cows have 12,000 liters milk in 305 days lactation period.',
        'breed_image':'http://antropocene.it/wp-content/uploads/2019/03/Razza-Ayrshire-800x445.jpg',   
    },
    {
        'breedname':'Guernsey',
        'description':'The milk is especially yellow, good herd produces on an average 4000 liters of milk on lactation, and the milk contains 5% fat. The highest milk production record in the breed in lactation of 365 days 13500 liters. The breed is losing in competition with other dairy and dual-purpose breeds.',
        'breed_image':'https://domesticanimalbreeds.com/wp-content/uploads/2019/01/Guernsey-Cattle-1024x586.jpg',
    },
    {
        'breedname':'Brown Swiss',
        'description':'The breed is a triple purpose animal in the homeland, i.e., milk, meat, and draught. In good herd average 5000 liters, milk produces per lactation, and it contains 4% milk fat.',
        'breed_image':'https://cdn.britannica.com/21/521-050-0C8E21D8/cow-Brown-Swiss.jpg',
    },
    {
        'breedname':'Milking Shorthorn',
        'description':'Milking Shorthorn is adapted in all climatic conditions. The cow is docile and calm temperament. The cows produce about 7000 liters of milk in annual lactation of 305 days.',
        'breed_image':'https://i2.wp.com/farminence.com/wp-content/uploads/2018/02/milking-shorthorn.jpg',
    },
    {
        'breedname':'American Milking Devon',
        'description':'The milk production capacity is very good, and from the pure herd, average milk production is around 5000-5500 liter, on an average of 23 liters daily. The milk fat is near about Jersey breed and ranges from 4.5 to 5.0 %.',
        'breed_image':'https://isteam.wsimg.com/ip/f18c2d9b-71a1-4e78-85f6-81db00a34b04/3f653083-ebf7-4568-a360-fe60bf783367.jpg/:/rs=h:650,cg:true,m',
    },
    {
        'breedname':'Normande Cattle',
        'description':'They are easy to handle because of hardy, docile and calm temperament. The cow produces 6000 liters of milk in lactation and on average daily milk production is about 20 liters. The milk contains a high percentage of protein and butterfat.',
        'breed_image':'https://normandegenetics.com/wp-content/uploads/2019/02/Lepanto.jpg',
    },
    {
        'breedname':'Norwegian Red',
        'description':'The Norwegian breed is a good milk producer, and cows produce around 10000 liters of milk in lactation. The best milk production recorded in lactation was 16000 liters, and milk contains good quality ingredients.',
        'breed_image':'https://www.norwegianred.com/globalassets/genointernational/geno_global/06_news/2020/08-11690roen.jpg',
    },
    {
        'breedname':'Red and White Holstein',
        'description':'The cattle is with black and patched white coat, occasionally red and white.  The cow,s weight is 600-700 kg, and the bull’s weight is larger than the cow. They are one of the most popular dairy cattle breeds of the world due to easily adaptable in all environments and high milk production.',
        'breed_image':'https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/2-red-and-white-holstein-heifer-judith-picciotto.jpg',
    },
]

indiandairyCows = [
    {
        'breedname':'Gir',
        'description':'This cattle breed originates from Gir forests of South Kathiawar in Gujarat and are also found in adjacent Rajasthan and Maharashtra. It is also known as Bhadawari, Desan, Gujarati, Sorthi, Kathiawari, and Surati. The horns of gir cattle are peculiarly curved, giving a ‘half moon’ appearance. Its milk yield ranges from 1200 to 1800 kilograms per lactation. This bread is recognized for its hardiness & disease resistance.',
        'breed_image':'https://www.agrifarming.in/wp-content/uploads/2018/06/Gir-Cow-Praject-Report.-1.jpg',
    },
    {
        'breedname':'Sahiwal',
        'description':'Sahiwal originated in the Montgomery region (now in Pakistan) of undivided India. This cattle breed is also known as Lola, Lambi Bar, Teli, Montgomery and Multani. Sahiwal is the best indigenous dairy breed in the country. The average milk yield of sahiwal is between 1400 & 2500 kilograms per lactation. Can be found in many parts of India like Haryana, Punjab, Delhi and Uttar Pradesh.',
        'breed_image':'http://www.atozpictures.com/uploads/2017/01/sahiwal-cow-animals-pictures.jpg',
    },
    {
        'breedname':'Red Sindhi',
        'description':'The red sindhi is mostly found in Karachi & Hyderabad district of neighboring Pakistan. It is also called as Sindhi and Red Karachi. The body colour of this cattle breed is basically red with shades varying from dark to red light and strips of white. Its milk yield ranges from 1100 to 2600 kilograms. Red sindhi is widely used in crossbreeding programmes.',
        'breed_image':'https://www.roysfarm.com/wp-content/uploads/2014/03/Red+Sindhi.jpg',   
    },
    {
        'breedname':'Rathi',
        'description':'Rathi is another milch cattle breed that is found in the dry regions of Rajasthan. This breed is believed to have evolved from amalgamation of Sahiwal, Red Sindhi, Tharparkar and Dhanni breeds with a prevalence of Sahiwal blood. The cattle are efficient and good milkers. They produce 1560 kilograms of milk and the lactation milk yield ranges from 1062 to 2810 kilograms.',
        'breed_image':'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Rathi_01.JPG/1200px-Rathi_01.JPG',
    },
    {
        'breedname':'Ongole',
        'description':'This cattle breed belongs to Ongole taluk in the Guntur district of Andhra Pradesh. They are large muscular cattle breeds with a well-developed hump. Ongole is suitable for heavy draught work. They are also known as Nellore and their average milk yield is 1000 kilograms / lactation.',
        'breed_image':'https://www.jagranjosh.com/imported/images/E/Others/ongole-cattle.JPG',
    },
    {
        'breedname':'Deoni',
        'description':'Deoni originated in Western Andhra Pradesh but is also found in the Marathwada region of Maharashtra and neighboring Karnataka. The milk yield of deoni ranges from 636 - 1230 kilograms per lactation and their caving interval average are 447 days. The bullocks are used for heavy cultivation.',
        'breed_image':'https://upload.wikimedia.org/wikipedia/commons/1/1d/Deoni_01.JPG',
    },
    {
        'breedname':'Kankrej',
        'description':'This cattle breed originated from Southeast Rann of Kutch, Gujarat and neighboring Rajasthan (Barmer & Jodhpur district). The colour of the cattle varies from silver-grey to iron-grey / steel black. Kankrej is quite popular as it is fast, powerful and draught cattle. It is used for ploughing and carting. The cows are also good milkers and yield about 1400 kilograms per lactation.',
        'breed_image':'https://img1.exportersindia.com/product_images/bc-full/dir_169/5068202/live-kankrej-cow-1500535568-3165496.jpeg',
    },
    {
        'breedname':'Tharparkar',
        'description':'This breed originated in Tharparkar district (Pak) of undivided India and is also found in Rajasthan. It is also known as Gray Sindhi, White Sindhi and Thari. Tharparkar are medium sized cattle, with lyre-shaped horn. Their body colour is white/light grey. The bullocks are suitable for ploughing & casting. In addition it yields 1800 to 2600 kilograms of milk/lactation.',
        'breed_image':'https://www.nativebreed.org/wp-content/uploads/2020/06/Tharparkar-cattle.jpg',
    },
    {
        'breedname':'Hariana',
        'description':'Hariana breed originated from Rohtak, Jind, Hisar, & Gurgaon districts of Haryana but are equally popular in Uttar Pradesh, Punjab and parts of Madhya Pradesh. The bullocks are considered as powerful work animals. Hariana cattle are fair milkers yielding 600 - 800 kilograms of milk per lactation.',
        'breed_image':'https://www.dairyknowledge.in/sites/default/files/styles/medium_large/public/hariana_cow.jpg?itok=hOOXA7nL',
    },
    {
        'breedname':'Krishna Valley',
        'description':'It has originated from black cotton soil of the watershed of river Krishna in Karnataka & also found in border districts of Maharashtra. The cattle are big in size, having a massive frame with deep, slackly built short body. Its tail reaches almost till the ground. The bullocks are very strong and thus used for ploughing & valued for their good working qualities. The average yield is 900 kilograms per lactation.',
        'breed_image':'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Krishna-cow_01.JPG/1200px-Krishna-cow_01.JPG',
    },
]
americandairyCows = [
    {
        'breedname':'Holstein Friesian',
        'description':'This breed is considered to be the best milk producer of the world and widely distributed in most countries of the world. Under tropical conditions, they may not perform well, since they are the least heat tolerant, but crossbred cows have yielded more than 46 litres of milk a day.',
        'breed_image':'https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/1-a-holstein-friesian-cow-in-the-green-field-isa-fernandez.jpg',
    },
    {
        'breedname':'Jersey',
        'description':'Although the milk yield is not high, the breed is popular all over the world. There are some reasons for popularity which include a high percentage of butter fats (5.3%) in the milk and compare to other breeds. Early maturity of heifers produces calf between 26-30 months and has a regular calving interval, after that 12 – 13 months. A good herd produces average about 4500 liters of milk in 300 days lactation period.',
        'breed_image':'https://cdn.britannica.com/22/522-050-25222A61/Jersey-cow.jpg',
    },
    {
        'breedname':'Brown Swiss',
        'description':'The breed is a triple purpose animal in the homeland, i.e., milk, meat, and draught. In good herd average 5000 liters, milk produces per lactation, and it contains 4% milk fat.',
        'breed_image':'https://cdn.britannica.com/21/521-050-0C8E21D8/cow-Brown-Swiss.jpg',   
    },
    {
        'breedname':'Guernsey',
        'description':'The milk is especially yellow, good herd produces on an average 4000 liters of milk on lactation, and the milk contains 5% fat. The highest milk production record in the breed in lactation of 365 days 13500 liters. The breed is losing in competition with other dairy and dual-purpose breeds.',
        'breed_image':'https://domesticanimalbreeds.com/wp-content/uploads/2019/01/Guernsey-Cattle-1024x586.jpg',
    },
    {
        'breedname':'Milking Shorthorn',
        'description':'Milking Shorthorn is adapted in all climatic conditions. The cow is docile and calm temperament. The cows produce about 7000 liters of milk in annual lactation of 305 days.',
        'breed_image':'https://i2.wp.com/farminence.com/wp-content/uploads/2018/02/milking-shorthorn.jpg',
    },
    {
        'breedname':'Ayrshire',
        'description':'The milk of Ayrshire breed contains an average of 4% fat. Though the milk quality is better than the Holstein, its lower potential yield has resulted in the Ayrshire being replaced by Holstein. However, the champion cows have 12,000 liters milk in 305 days lactation period.',
        'breed_image':'http://antropocene.it/wp-content/uploads/2019/03/Razza-Ayrshire-800x445.jpg',
    },
    {
        'breedname':'Red and White Holstein',
        'description':'The cattle is with black and patched white coat, occasionally red and white.  The cow,s weight is 600-700 kg, and the bull’s weight is larger than the cow. They are one of the most popular dairy cattle breeds of the world due to easily adaptable in all environments and high milk production.',
        'breed_image':'https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/2-red-and-white-holstein-heifer-judith-picciotto.jpg',
    },
]

commondairyCows = [
    {
        'breedname':'Angus',
        'description':'Black Angus cattle, also called Aberdeen Angus, are the most popular breed in the U.S., and thanks to some excellent marketing, their meat is in demand, which means these cattle -- and crossbreds with mostly black markings -- often bring a premium at the sale barn. This breed comes from northeastern Scotland and was first brought to the U.S. by a Kansas rancher in 1873. When crossed with Texas longhorn cows, the hornless black calves brought winter hardiness to the mix. Angus are naturally polled (hornless), and have black skin and hair. They are moderately sized, generally good mothers, and are known for early development, ease of fleshing, good milk supply, and excellent marbling.',
        'breed_image':'https://factfile.org/wp-content/uploads/2015/02/Angus-Cattle-Pic.jpg',
    },
    {
        'breedname':'Belted Galloway',
        'description':'Commonly called "Oreo cattle" because of their black color (possibly brown or red) with a white stripe through their middles, this breed started in Scotland as a solid-color cow, but got their belts through the introduction of Dutch Belted blood. They were first imported to the U.S. in 1950. Although Belted Galloways are often purchased for their ornamental qualities, they do produce lean, quality beef. They\'re a medium-sized breed, but their carcass dressed weights can exceed 60% of their live weight. Belties have a double coat of hair, which allows them to keep warm in the winter without developing a layer of backfat like some other breeds.',
        'breed_image':'https://millersofspeyside.co.uk/wp-content/uploads/2020/03/Belted-Galloway-Cow.jpg',
    },
    {
        'breedname':'Brahman',
        'description':'Brahman cattle come from India, and are the most common cattle breed in the world. Over the centuries, Brahmans have developed resistance to pests, parasites, and diseases, and the ability to survive inadequate food and harsh weather. They have a large hump over their shoulder and neck, upward-curving horns, large ears, and excess skin under their necks and chests, which helps keep them cool. They also are able to sweat better than most cattle, and secrete an oil which helps repel insects.',
        'breed_image':'https://morenoranches.com/wp-content/uploads/2018/05/734.jpg',   
    },
    {
        'breedname':'Charolais',
        'description':'The light-colored Charolais originated in France, where it was used for meat, milk, and drafting. The animals large size and sturdy frame gave them the power to work in fields and pull wagons. The first Charolais came into the U.S. by way of Mexico in the 1930s. Because of a disease outbreak in Mexico, the breed was not allowed to be imported to North America until 1965. Therefore, many of today\'s American Charolais have other breeds in their lineage as well. Charolais do well under a variety of environmental conditions. They graze aggressively in warm weather, withstand the cold, and have heavy calves. For this reason, adding a Charolais bull to a herd can improve the size and ruggedness of calves.',
        'breed_image':'https://charolais.com.au/wp-content/uploads/2019/05/LOT-47-GLE-J8E-1-1024x683.jpg',
    },
    {
        'breedname':'Dexter',
        'description':'Dexter cattle originated in southern Ireland, and came to the U.S. in the early 1900s. They are one of the smallest breeds of cattle, with full-grown bulls measuring 38 to 44 inches at the shoulder and weighing less than 1,000 pounds. Some have long legs and some short. Because of their size, they require less pasture and feed than larger breeds. They thrive in hot and cold climates, and are known for being gentle and easy to handle. Dexters have a high rate of fertility and are easy calvers. They can be raised for both milk and meat. They can produce more milk for their weight than any other breed, and their milk yields up to a quart of cream per gallon. Their beef is slightly darker red than other breeds, and the small cuts are lean and graded choice.',
        'breed_image':'https://dextersintasmania.weebly.com/uploads/5/9/1/4/5914447/6332834_orig.jpg',
    },
    {
        'breedname':'GELBVIEH',
        'description':'This breed originated in Baravia, in southern Germany, and was originally developed for meat, milk, and work. It was introduced to the U.S. in 1971, through an artificial insemination program. Females are registered as purebred at 7/8 Gelbvieh, and bulls at 15/16. Bulls in Germany must undergo extensive tests to become A.I. sires. Gelbviehs are red, with pigmented skin, and were originally horned. Due to breeding with polled foundation females in the U.S., though, many today are naturally polled. They are known for high fertility, ease of calving, being good mothers, and having quick-growing calves.',
        'breed_image':'https://orsd-web.imgix.net/judd/web/Photos/Gelbvieh%20Females/JRI9M11_horizontal_08.jpg',
    },
    {
        'breedname':'Hereford',
        'description':'The Hereford breed was developed in England in the 1700s to fulfill the expanding food market created by the industrial revolution. The original Herefords were bred for a high yield of beef and efficient production, and those characteristics are still important in the breed today. They were brought to the U.S. in 1817 and were useful for improving herds in the Southwest. Because of their early maturity and fattening ability, Herefords became very popular in the U.S. As tastes changed in the 1950s, Herefords were bred to be leaner, with less fat and more red meat. Both horned and polled Herefords remain common in the U.S. They are known for their longevity, and for being docile, easy calvers, good milkers, and good mothers.',
        'breed_image':'https://www.cows.ie/wp-content/uploads/2018/08/Hereford-cow-pinterest-1024x769.jpg',
    },
    {
        'breedname':'Holstein Friesian',
        'description':'This breed is considered to be the best milk producer of the world and widely distributed in most countries of the world. Under tropical conditions, they may not perform well, since they are the least heat tolerant, but crossbred cows have yielded more than 46 litres of milk a day.',
        'breed_image':'https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/1-a-holstein-friesian-cow-in-the-green-field-isa-fernandez.jpg',
    },
]


#  VIEWS

def dairycows(request):
    context = { 'dairyCows':dairyCows }
    return render(request,'cows/dairycows.html',context)

def indiandairycows(request):
    context = { 'indiandairyCows':indiandairyCows }
    return render(request,'cows/indiandairycows.html',context)

def americandairycows(request):
    context = {'americandairyCows':americandairyCows}
    return render(request,'cows/americandairycows.html',context)

def commondairycows(request):
    context = {'commondairyCows':commondairyCows}
    return render(request,'cows/mccb.html',context)

def cowtypes(request):
    all_cows = Cattle.objects.all
    return render(request,'cows/cowtypes.html',{'all':all_cows})

def cowsdetailed(request,id):
    cow_searched = Cattle.objects.get(pk=id)
    return render(request,'cows/cows_detailed.html',{'cow_searched':cow_searched})

def addcowcomment(request,id):
    form = AddCattleComment()

    if request.method == 'POST':
        form = AddCattleComment(request.POST)

        if form.is_valid():
            form.instance.cattle_id = id
            form.save(commit=True)
            return render(request,'homepage/index.html')

    return render(request,'cows/cow_comment_section.html',{'form':form})
