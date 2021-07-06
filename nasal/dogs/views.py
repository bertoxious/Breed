from django.shortcuts import render
from homepage.models import Dog
from dogs.forms import AddDogComment

##Dictionaries
popularDogs = [
    {
        'breedname':'LABRADOR RETRIEVER',
        'description':'The sweet-faced, lovable Labrador Retriever is America\'s most popular dog breed. Labs are friendly, outgoing, and high-spirited companions who have more than enough affection to go around for a family looking for a medium-to-large dog.',
        'breed_image':'http://www.reportingday.com/wp-content/uploads/2018/07/Labrador-Retriever-Dog-HD-Wallpapers.jpg',
    },
    {
        'breedname':'GERMAN SHEPHERD',
        'description':'German Shepherd Dogs can stand as high as 26 inches at the shoulder and, when viewed in outline, presents a picture of smooth, graceful curves rather than angles. The natural gait is a free-and-easy trot, but they can turn it up a notch or two and reach great speeds.',
        'breed_image':'http://vignette3.wikia.nocookie.net/thecompletedog/images/d/dd/German_shepherd.jpg/revision/latest?cb=20140204210455',
    },
    {
        'breedname':'GOLDEN RETRIEVER',
        'description':'The Golden Retriever is a medium-large gun dog that was bred to retrieve shot waterfowl, such as ducks and upland game birds, during hunting and shooting parties. The name "retriever" refers to the breed\'s ability to retrieve shot game undamaged due to their soft mouth.',
        'breed_image':'https://d1dd4ethwnlwo2.cloudfront.net/wp-content/uploads/2020/11/10-golden-retriever-rescues-7.jpg',   
    },
    {
        'breedname':'FRENCH BULLDOG',
        'description':'The French Bulldog has enjoyed a long history as a companion dog. Created in England to be a miniature Bulldog, they accompanied English lacemakers to France, where they acquired their “Frenchie” moniker.',
        'breed_image':'https://www.snopes.com/tachyon/2019/12/Getty-French-Bulldogs.jpg?fit=1200,648',
    },
    {
        'breedname':'BULLDOG',
        'description':'The Bulldog, also known as the English Bulldog or British Bulldog, is a medium-sized dog breed. It is a muscular, hefty dog with a wrinkled face and a distinctive pushed-in nose. The Kennel Club, the American Kennel Club, and the United Kennel Club oversee breeding records.',
        'breed_image':'https://i0.wp.com/www.mascotarios.org/wp-content/uploads/2012/03/BulldogIngles.jpg',
    },
    {
        'breedname':'POODLE',
        'description':'The Poodle, called the Pudel in German and the Caniche in French, is a breed of water dog. The breed is divided into four varieties based on size, the Standard Poodle, Medium Poodle, Miniature Poodle and Toy Poodle, although the Medium Poodle variety is not universally recognised.',
        'breed_image':'https://dogfriendlyscene.co.uk/wp-content/uploads/2020/09/Poodle-Puppy.png',
    },
    {
        'breedname':'BEAGLE',
        'description':'Small, compact, and hardy, Beagles are active companions for kids and adults alike. Canines of this dog breed are merry and fun loving, but being hounds, they can also be stubborn and require patient, creative training techniques.',
        'breed_image':'https://static.dailyforest.com/wp-content/uploads/2016/01/26150425/Beagle.jpg',
    },
    {
        'breedname':'ROTTWEILER',
        'description':'The Rottweiler is a robust working breed of great strength descended from the mastiffs of the Roman legions. A gentle playmate and protector within the family circle, the Rottie observes the outside world with a self-assured aloofness.',
        'breed_image':'https://highwaymail.co.za/wp-content/uploads/sites/50/2015/06/dog.jpg',
    },
    {
        'breedname':'GERMAN SHORTHAIRED POINTERS',
        'description':'This energetic, intelligent dog is enthusiastic at work and play. He likes being with people and is a good friend to children, albeit a bit rambunctious for little ones. That people-loving personality causes the GSP to be unhappy if left alone for long periods, and he can become nervous and destructive if he\'s not provided with regular companionship and exercise.',
        'breed_image':'https://vetstreet.brightspotcdn.com/dims4/default/232fcc6/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https:%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fda%2Fa44590a0d211e0a2380050568d634f%2Ffile%2FGerman-Shorthair-Pointer-2-645mk062111.jpg',
    },
    {
        'breedname':'PEMBROKE WELSH CORGI',
        'description':'The Pembroke Welsh Corgi is a cattle herding dog breed that originated in Pembrokeshire, Wales. It is one of two breeds known as a Welsh Corgi. The other is the Cardigan Welsh Corgi, and both descend from the line of northern spitz-type dogs.',
        'breed_image':'https://www.kingstonvetclinic.com/wp-content/uploads/sites/50/2020/01/1912_Breeds_Corgi_GettyImages-1061822700.png',
    },
]
easytotrainDogs = [
    {
        'breedname':'POODLE',
        'description':'The Poodle, called the Pudel in German and the Caniche in French, is a breed of water dog. The breed is divided into four varieties based on size, the Standard Poodle, Medium Poodle, Miniature Poodle and Toy Poodle, although the Medium Poodle variety is not universally recognised.',
        'breed_image':'https://dogfriendlyscene.co.uk/wp-content/uploads/2020/09/Poodle-Puppy.png',
    },
    {
        'breedname':'GOLDEN RETRIEVER',
        'description':'The Golden Retriever is a medium-large gun dog that was bred to retrieve shot waterfowl, such as ducks and upland game birds, during hunting and shooting parties. The name "retriever" refers to the breed\'s ability to retrieve shot game undamaged due to their soft mouth.',
        'breed_image':'https://d1dd4ethwnlwo2.cloudfront.net/wp-content/uploads/2020/11/10-golden-retriever-rescues-7.jpg',
    },
    {
        'breedname':'LABRADOR RETRIEVER',
        'description':'The sweet-faced, lovable Labrador Retriever is America\'s most popular dog breed. Labs are friendly, outgoing, and high-spirited companions who have more than enough affection to go around for a family looking for a medium-to-large dog.',
        'breed_image':'http://www.reportingday.com/wp-content/uploads/2018/07/Labrador-Retriever-Dog-HD-Wallpapers.jpg',   
    },
    {
        'breedname':'COLLIE',
        'description':'Both the Smooth and Rough Collies are large herding dogs that were bred to be independent workers yet sensitive to their owner’s needs. They are intelligent dogs that are easy to train as they are not so energetic that the average owner will not have trouble keeping up.',
        'breed_image':'https://www.petpaw.com.au/wp-content/uploads/2015/05/Lovely-Scotch-Collie.jpg',
    },
    {
        'breedname':'GERMAN SHEPHERD',
        'description':'German Shepherd Dogs can stand as high as 26 inches at the shoulder and, when viewed in outline, presents a picture of smooth, graceful curves rather than angles. The natural gait is a free-and-easy trot, but they can turn it up a notch or two and reach great speeds.',
        'breed_image':'http://vignette3.wikia.nocookie.net/thecompletedog/images/d/dd/German_shepherd.jpg/revision/latest?cb=20140204210455',
    },
    {
        'breedname':'CARDIGAN WELSH CORGI',
        'description':'The older and larger of the Corgis, the Cardigan Welsh Corgi is a strong-willed, independent herding dog but is intelligent and sensitive to their owners. They need a job and enjoy learning new behaviors, so basic obedience and house manners should be a breeze.',
        'breed_image':'https://www.101dogbreeds.com/wp-content/uploads/2018/08/Cardigan-Welsh-Corgi-Puppy.jpg',
    },
    {
        'breedname':'SHETLAND SHEEPDOG',
        'description':'The Shetland Sheepdog appears to be a smaller version of the Rough Collie, but they are slightly more active and do well in various dog sports. They are intelligent and eager to please, making them easy to train.',
        'breed_image':'https://thehappypuppysite.com/wp-content/uploads/2019/02/Shetland-Sheepdog-Temperament-long-1.jpg',
    },
    {
        'breedname':'PAPILLON',
        'description':'Most toy breeds are stubborn and difficult to work with, but the Papillon is a hidden gem in the group. These dogs are very intelligent and quite eager to please. Small but active. this is a breed that enjoys learning new behaviors and does very well in various dog sports.',
        'breed_image':'https://cutehomepets.com/wp-content/uploads/2020/03/245178-2121x1414-papillon-looking-up.jpg',
    },
    {
        'breedname':'SWIDISH VALLHUND',
        'description':'Similar to the Corgis, Swedish Vallhunds are a dwarfed herding breed that were bred to work independently but pay attention to their owner’s desires. They are active and intelligent dogs that need a consistent owner but are relatively easy to train.',
        'breed_image':'https://a-z-animals.com/media/swedish-vallhund-4.jpg',
    },
    {
        'breedname':'PEMBROKE WELSH CORGI',
        'description':'The Pembroke Welsh Corgi is a cattle herding dog breed that originated in Pembrokeshire, Wales. It is one of two breeds known as a Welsh Corgi. The other is the Cardigan Welsh Corgi, and both descend from the line of northern spitz-type dogs.',
        'breed_image':'https://www.kingstonvetclinic.com/wp-content/uploads/sites/50/2020/01/1912_Breeds_Corgi_GettyImages-1061822700.png',
    },
]

largestDogs = [
    {
        'breedname':'S.T. BERNARD',
        'description':'St. Bernard’s height varies between 69 to 89 cm and they weigh around 73 to 117 kg.  These are giant, big dogs, bred to work! They are well-known for having performed rescue jobs in the Swiss Alps! And with the right training, they will be very friendly and loyal to their owners.',
        'breed_image':'https://www.zastavki.com/pictures/1920x1200/2012/Animals_Dogs_St._Bernards_034270_.jpg',
    },
    {
        'breedname':'NEWFOUNDLAND',
        'description':'Newfoundlands are massive dogs, their weight comes around 118 kg while their height may be around 183 cm, from nose to tail! They are working dogs and great swimmers – therefore, famous for performing water jobs, rescue, and sports! They have earned the name Gentle Giants for a reason – they are extremely loving towards their families.',
        'breed_image':'https://www.mypetzilla.co.uk/files/4115/4170/3046/Newfoundland_Dog.jpg',
    },
    {
        'breedname':'GREAT DANE',
        'description':'Great Danes have earned the reputation of being the tallest dog breed in the world! Their height can reach about 76-87 cm, while their weight between 54-90 kg. Danes were firstly bred for hunting purposes, although over time they have become exceptional companion dogs! Great Dane is one of the most Dangerous Dogs in the World.',
        'breed_image':'https://thefreshtoast.com/wp-content/uploads/2018/06/dogs-of-instagram-great-dane.jpg',   
    },
    {
        'breedname':'FRENCH MASTIFF',
        'description':'French Mastiff or otherwise known as Dogue de Bordeaux – weighs around 54-66 kg, whereas their height stands between 58 and 76cm! These dogs are very powerful as well as fearless, which makes up for the perfect guard dogs.',
        'breed_image':'https://www.europuppy.com/wp-content/uploads/desc160-1024x640.jpg',
    },
    {
        'breedname':'ANATOLIAN SHEPHERD',
        'description':'Anatolian Shepherds originate from Turkey and are used for guarding sheep against predators, such as wolves, bears, and even cheetahs! They are strong, muscular dogs that weight around 41 to 68 kg, while they stand between 76 up to 92 cm tall! These dogs have a fearless protective instinct, but they are also very loving and loyal towards their pack.',
        'breed_image':'https://www.nativebreed.org/wp-content/uploads/2020/06/Anatolian-Shepherd-Dog.jpeg',
    },
    {
        'breedname':'LEONBERGER',
        'description':'Leonbergers have been bred by mixing three of the largest dogs, the Newfoundland, Great Pyrenees, and the St. Bernard, no wonder they are large and proud dogs, weighing around 54-77 kg, while their height varies between 71-80 cm',
        'breed_image':'https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555345659/shape/mentalfloss/istock_000027869640_small.jpg',
    },
    {
        'breedname':'ENGLISH MASTIFF',
        'description':'Mastiffs are the largest dogs concerning mass, but not height! They weigh between 50 to 156 kg, while they stand around 64 to 91 cm tall! They have served as watchdogs for most of their existence, even Caeser of Rome was impressed with their appearance and performance during the conquest of England!',
        'breed_image':'https://www.zooplus.ie/magazine/content/uploads/2018/12/English-Mastiff-Dog-Breed-1024x681.jpg',
    },
    {
        'breedname':'LANDSEER',
        'description':'Landseer dogs are very similar to Newfoundland dogs that sometimes they are mistakenly considered one same breed, although they do have a few differences in appearance and personality! Overall, they are sweet and gentle dogs and easier to train! They weight around 82 kg and are about 82 cm tall! They make perfect lifeguards, rescuing people from drowning!',
        'breed_image':'https://2.bp.blogspot.com/-pYW9lo83-7M/UP7nvBNT5VI/AAAAAAAAAOc/1k95Oqe7i7c/s1600/mauritz+wei.jpg',
    },
    {
        'breedname':'KANGAL',
        'description':'Kangals originate from Turkey and they are well-known livestock guardian dogs! These dogs are not as massive as other Mastiff breeds, which makes them faster and more agile! They weigh around 66 kg, whereas their height varies between 76 and 81 cm!',
        'breed_image':'https://image.winudf.com/v2/image1/Y29tLndhbGxwYXBlcnMua2FuZ2FsZHV2YXJrYWdpdGxhcmlfc2NyZWVuXzZfMTU1OTY4OTI3MF8wNTQ/screen-6.jpg?fakeurl=1&type=.jpg',
    },
    {
        'breedname':'TIBETIAN MASTIFF',
        'description':'Tibetan Mastiffs, although not actually Mastiffs, are flock guardian dogs that are fearless to confront some of the strongest predators, like the wolf and the leopard.They are muscular, large dogs – weighing between 45-72 kg and standing around 84 cm tall',
        'breed_image':'https://4.bp.blogspot.com/-f15EIdejmjs/UaQcUXscGrI/AAAAAAAADOo/tM9Qp9DuLEs/s1600/Tibetan-Mastiff-Nice-Dog.jpg',
    },
]

swimmerDogs = [
    {
        'breedname':'CHESAPEAKE BAY RETRIEVER',
        'description':'These dogs just LOVE water! They can do great work in water and are very tolerable of cold weather conditions. Dog owners must include water exercises and activities if considering to get a “Chessie”.',
        'breed_image':'https://www.thesprucepets.com/thmb/TV0QFYU7Ujl2Haf04Ljk3uKMuI8=/2121x1414/filters:fill(auto,1)/ktatarka-c351d1c8c0d444fbb05ef0d0669eb3c5.jpg',
    },
    {
        'breedname':'LABRADOR RETRIEVER',
        'description':'The sweet-faced, lovable Labrador Retriever is America\'s most popular dog breed. Labs are friendly, outgoing, and high-spirited companions who have more than enough affection to go around for a family looking for a medium-to-large dog.',
        'breed_image':'http://www.reportingday.com/wp-content/uploads/2018/07/Labrador-Retriever-Dog-HD-Wallpapers.jpg',
    },
    {
        'breedname':'GOLDEN RETRIEVER',
        'description':'The Golden Retriever is a medium-large gun dog that was bred to retrieve shot waterfowl, such as ducks and upland game birds, during hunting and shooting parties. The name "retriever" refers to the breed\'s ability to retrieve shot game undamaged due to their soft mouth.',
        'breed_image':'https://d1dd4ethwnlwo2.cloudfront.net/wp-content/uploads/2020/11/10-golden-retriever-rescues-7.jpg',   
    },
    {
        'breedname':'NEWFOUNDLAND',
        'description':'Newfoundlands are massive dogs, their weight comes around 118 kg while their height may be around 183 cm, from nose to tail! They are working dogs and great swimmers – therefore, famous for performing water jobs, rescue, and sports! They have earned the name Gentle Giants for a reason – they are extremely loving towards their families.',
        'breed_image':'https://www.mypetzilla.co.uk/files/4115/4170/3046/Newfoundland_Dog.jpg',
    },
    {
        'breedname':'PORTUGUESE WATER DOG',
        'description':'These dogs are known to herd fish into nets as well as being couriers from ships to shore. If you are thinking about getting a Portuguese Water Dog, make room for water activities, as these dogs enjoy doing what they have been bred to do.',
        'breed_image':'https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/v1555377343/shape/mentalfloss/istock_000041230288_small.jpg?itok=anx0vWJf',
    },
    {
        'breedname':'POODLE',
        'description':'The Poodle, called the Pudel in German and the Caniche in French, is a breed of water dog. The breed is divided into four varieties based on size, the Standard Poodle, Medium Poodle, Miniature Poodle and Toy Poodle, although the Medium Poodle variety is not universally recognised.',
        'breed_image':'https://dogfriendlyscene.co.uk/wp-content/uploads/2020/09/Poodle-Puppy.png',
    },
    {
        'breedname':'NOVA SCOTIA DUCK TOLLING RETRIEVER',
        'description':'Developed since the 19th century to retrieve waterfowl, these dogs, even though the smallest of the retrievers in size, make amazing swimmers and jumpers.',
        'breed_image':'https://researchbreeder.com/images/Breed%20Pictures/N/nova-scotia-duck-tolling-retriever.jpg',
    },
    {
        'breedname':'IRISH WATER SPANIEL',
        'description':'Clever, intelligent and with distinctive water-repellant curly coats, these dogs make for expert water hunters. Think of their love of water whenever you think about adopting a beauty like this.',
        'breed_image':'https://www.petguide.com/wp-content/uploads/2013/04/irish-water-spaniel-1.jpg',
    },
    {
        'breedname':'ENGLISH SETTER',
        'description':'Once these dogs find water, you will not be able to get them out easily! They are overly energetic, so swimming is one recommended activity',
        'breed_image':'https://fishsubsidy.org/wp-content/uploads/2020/02/english-setter-characterstics.jpg',
    },
]
# Create your views here.

def newten(request):
    return render(request,'dogs/newten.html')

def topten(request):
    context = { 'popularDogs':popularDogs }
    return render(request,'dogs/topten.html',context)

def easy(request):
    context = { 'easytotrainDogs':easytotrainDogs }
    return render(request,'dogs/easytotraindogs.html',context)

def largestdogs(request):
    context = { 'largestDogs':largestDogs }
    return render(request,'dogs/largestdogs.html',context)

def swimmerdogs(request):
    context = { 'swimmerDogs':swimmerDogs }
    return render(request,'dogs/swimmerdogs.html',context)

def dogtypes(request):
    all_dogs = Dog.objects.all
    return render(request,'dogs/dogtypes.html',{'all':all_dogs})

def dogsdetailed(request,id):
    dogs_searched = Dog.objects.get(pk=id)
    return render(request,'dogs/dogs-detailed.html',{'dogs_searched':dogs_searched})

def adddogcomment(request,id):
    form = AddDogComment()

    if request.method == 'POST':
        form = AddDogComment(request.POST)


        if form.is_valid():
            form.instance.dog_id = id
            form.save(commit=True)
            return render(request,'homepage/index.html')

    return render(request,'dogs/dog_comment_section.html',{'form':form})
