from models import PlaceModel



PLACES_DATABASE = {
    "goa":[
        PlaceModel(
            name="Baga Beach",
            description="A popular beach in North Goa known for its nightlife and water sports.",
            category="Beach",
            rating=4.5,
            estimated_time_hours=3.0,
            entry_fee=None
        ),
        PlaceModel(
            name="Fort Aguada",
            description="A well-preserved 17th-century Portuguese fort overlooking the Arabian Sea.",
            category="Historical Site",
            rating=4.7,
            estimated_time_hours=2.0,
            entry_fee=10.0
        ),
        PlaceModel(
            name="Dudhsagar Waterfalls",
            description="A majestic waterfall located on the Mandovi River, surrounded by lush greenery.",
            category="Nature",
            rating=4.8,
            estimated_time_hours=4.0,
            entry_fee=5.0
        ),
        PlaceModel(
            name="Basilica of Bom Jesus",
            description="A UNESCO World Heritage Site and a significant Christian pilgrimage site.",
            category="Religious Site",
            rating=4.6,
            estimated_time_hours=1.5,
            entry_fee=None
        ),
        PlaceModel(
            name="Anjuna Flea Market",
            description="A vibrant market offering a variety of goods, from handicrafts to clothing.",
            category="Shopping",
            rating=4.3,
            estimated_time_hours=2.0,
            entry_fee=None
        ),
        PlaceModel(
            name="Chapora Fort",
            description="A historic fort offering panoramic views of the surrounding area and the Arabian Sea.",
            category="Historical Site",
            rating=4.4,
            estimated_time_hours=2.5,
            entry_fee=None
        )
    ],
    "delhi": [
        PlaceModel(name="Red Fort", description="A UNESCO-listed Mughal fort and landmark in Old Delhi.", category="Historical Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Qutub Minar", description="A UNESCO-listed medieval minaret surrounded by historic ruins.", category="Historical Site", rating=4.6, estimated_time_hours=2.0),
        PlaceModel(name="Humayun's Tomb", description="A landmark Mughal garden tomb and UNESCO World Heritage Site.", category="Historical Site", rating=4.7, estimated_time_hours=2.0),
        PlaceModel(name="India Gate", description="A war memorial on a broad ceremonial avenue in central Delhi.", category="Landmark", rating=4.5, estimated_time_hours=1.0),
    ],
    "mumbai": [
        PlaceModel(name="Gateway of India", description="A grand waterfront arch and one of Mumbai's best-known landmarks.", category="Landmark", rating=4.6, estimated_time_hours=1.0),
        PlaceModel(name="Elephanta Caves", description="A UNESCO-listed cave complex with historic rock-cut sculptures.", category="Historical Site", rating=4.5, estimated_time_hours=4.0),
        PlaceModel(name="Chhatrapati Shivaji Maharaj Terminus", description="A UNESCO-listed Victorian Gothic railway station.", category="Historical Site", rating=4.6, estimated_time_hours=1.0),
        PlaceModel(name="Marine Drive", description="A curving seafront promenade popular for sunset walks.", category="Nature", rating=4.6, estimated_time_hours=1.5),
    ],
    "jaipur": [
        PlaceModel(name="Amber Fort", description="A hilltop fort and palace known for its courtyards and ornate halls.", category="Historical Site", rating=4.7, estimated_time_hours=3.0),
        PlaceModel(name="Hawa Mahal", description="An iconic pink sandstone palace façade with many small windows.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="City Palace", description="A royal complex with courtyards, museums, and historic architecture.", category="Historical Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Jantar Mantar", description="A UNESCO-listed collection of historic astronomical instruments.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
    ],
    "agra": [
        PlaceModel(name="Taj Mahal", description="A UNESCO-listed marble mausoleum and one of India's most recognized monuments.", category="Historical Site", rating=4.9, estimated_time_hours=3.0),
        PlaceModel(name="Agra Fort", description="A historic Mughal fort overlooking the Yamuna River.", category="Historical Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Fatehpur Sikri", description="A UNESCO-listed former Mughal capital with palaces and courtyards.", category="Historical Site", rating=4.6, estimated_time_hours=3.0),
        PlaceModel(name="Mehtab Bagh", description="A riverside garden offering views of the Taj Mahal.", category="Nature", rating=4.4, estimated_time_hours=1.5),
    ],
    "varanasi": [
        PlaceModel(name="Dashashwamedh Ghat", description="A central riverside ghat known for its evening Ganga Aarti.", category="Religious Site", rating=4.7, estimated_time_hours=2.0),
        PlaceModel(name="Kashi Vishwanath Temple", description="A major Hindu pilgrimage temple dedicated to Lord Shiva.", category="Religious Site", rating=4.7, estimated_time_hours=2.0),
        PlaceModel(name="Sarnath", description="An important Buddhist pilgrimage site where the Buddha gave his first sermon.", category="Historical Site", rating=4.6, estimated_time_hours=3.0),
        PlaceModel(name="Assi Ghat", description="A lively southern ghat popular for riverfront walks and boat rides.", category="Nature", rating=4.5, estimated_time_hours=1.5),
    ],
    "udaipur": [
        PlaceModel(name="City Palace", description="A lakeside palace complex with courtyards, galleries, and city views.", category="Historical Site", rating=4.7, estimated_time_hours=3.0),
        PlaceModel(name="Lake Pichola", description="A scenic lake known for boat rides and views of the old city.", category="Nature", rating=4.7, estimated_time_hours=2.0),
        PlaceModel(name="Jag Mandir", description="A historic island palace set on Lake Pichola.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Saheliyon-ki-Bari", description="A historic garden with fountains, pools, and shaded paths.", category="Nature", rating=4.4, estimated_time_hours=1.5),
    ],
    "jodhpur": [
        PlaceModel(name="Mehrangarh Fort", description="A hilltop fort with museums and sweeping views of the blue city.", category="Historical Site", rating=4.8, estimated_time_hours=3.0),
        PlaceModel(name="Jaswant Thada", description="A white marble memorial set among gardens near Mehrangarh Fort.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Umaid Bhawan Palace", description="A landmark palace with a museum documenting royal history.", category="Historical Site", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Clock Tower and Sardar Market", description="A lively market area known for spices, textiles, and local goods.", category="Shopping", rating=4.3, estimated_time_hours=2.0),
    ],
    "amritsar": [
        PlaceModel(name="Golden Temple", description="The holiest shrine of Sikhism, set beside the sacred pool of Amrit Sarovar.", category="Religious Site", rating=4.9, estimated_time_hours=3.0),
        PlaceModel(name="Jallianwala Bagh", description="A memorial garden commemorating the 1919 massacre.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Wagah-Attari Border", description="A border crossing known for its daily flag-lowering ceremony.", category="Cultural Site", rating=4.5, estimated_time_hours=3.0),
        PlaceModel(name="Partition Museum", description="A museum documenting the stories and impact of the 1947 Partition.", category="Cultural Site", rating=4.6, estimated_time_hours=2.0),
    ],
    "kochi": [
        PlaceModel(name="Fort Kochi", description="A historic waterfront neighborhood with colonial-era streets and cafés.", category="Cultural Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Chinese Fishing Nets", description="Distinctive shore-operated fishing nets along the Fort Kochi waterfront.", category="Landmark", rating=4.4, estimated_time_hours=1.0),
        PlaceModel(name="Mattancherry Palace", description="A historic palace museum known for its murals and collections.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Jew Town and Paradesi Synagogue", description="A historic quarter with antique shops and a landmark synagogue.", category="Cultural Site", rating=4.4, estimated_time_hours=2.0),
    ],
    "bengaluru": [
        PlaceModel(name="Lalbagh Botanical Garden", description="A historic botanical garden with a glasshouse and diverse plant collections.", category="Nature", rating=4.5, estimated_time_hours=2.5),
        PlaceModel(name="Bengaluru Palace", description="A Tudor-style palace with decorated interiors and landscaped grounds.", category="Historical Site", rating=4.3, estimated_time_hours=2.0),
        PlaceModel(name="Cubbon Park", description="A large green space in the city center with walking paths and public buildings.", category="Nature", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Vidhana Soudha", description="A prominent government building and example of Neo-Dravidian architecture.", category="Landmark", rating=4.4, estimated_time_hours=1.0),
    ],
    "hyderabad": [
        PlaceModel(name="Charminar", description="A 16th-century monument and landmark in Hyderabad's old city.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Golconda Fort", description="A historic fort known for its architecture and panoramic city views.", category="Historical Site", rating=4.6, estimated_time_hours=3.0),
        PlaceModel(name="Salar Jung Museum", description="A major museum with collections of art, antiques, and historic objects.", category="Cultural Site", rating=4.5, estimated_time_hours=3.0),
        PlaceModel(name="Chowmahalla Palace", description="A restored palace complex that was once the seat of the Nizams.", category="Historical Site", rating=4.5, estimated_time_hours=2.0),
    ],
    "chennai": [
        PlaceModel(name="Marina Beach", description="A long urban beach and popular public promenade along the Bay of Bengal.", category="Beach", rating=4.3, estimated_time_hours=2.0),
        PlaceModel(name="Kapaleeshwarar Temple", description="A historic Dravidian-style temple dedicated to Lord Shiva.", category="Religious Site", rating=4.6, estimated_time_hours=1.5),
        PlaceModel(name="Fort St. George", description="A historic British fort complex that houses a museum and government offices.", category="Historical Site", rating=4.3, estimated_time_hours=2.0),
        PlaceModel(name="Government Museum", description="A museum complex with archaeology, art, and natural history galleries.", category="Cultural Site", rating=4.3, estimated_time_hours=2.5),
    ],
    "kolkata": [
        PlaceModel(name="Victoria Memorial", description="A marble memorial and museum set within landscaped gardens.", category="Historical Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Howrah Bridge", description="An iconic cantilever bridge spanning the Hooghly River.", category="Landmark", rating=4.5, estimated_time_hours=1.0),
        PlaceModel(name="Dakshineswar Kali Temple", description="A riverside Hindu temple complex dedicated to Goddess Kali.", category="Religious Site", rating=4.6, estimated_time_hours=2.0),
        PlaceModel(name="Indian Museum", description="One of India's oldest museums, with art, archaeology, and natural history galleries.", category="Cultural Site", rating=4.4, estimated_time_hours=2.5),
    ],
    "mysuru": [
        PlaceModel(name="Mysore Palace", description="A grand royal palace known for its architecture and illuminated evening display.", category="Historical Site", rating=4.8, estimated_time_hours=2.5),
        PlaceModel(name="Chamundi Hill", description="A hilltop temple and viewpoint overlooking Mysuru.", category="Religious Site", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Brindavan Gardens", description="A landscaped garden beside the Krishna Raja Sagara Dam.", category="Nature", rating=4.3, estimated_time_hours=2.0),
        PlaceModel(name="Devaraja Market", description="A traditional market known for flowers, produce, spices, and local goods.", category="Shopping", rating=4.3, estimated_time_hours=1.5),
    ],
    "pune": [
        PlaceModel(name="Shaniwar Wada", description="A historic fortification and palace associated with the Peshwas.", category="Historical Site", rating=4.4, estimated_time_hours=1.5),
        PlaceModel(name="Aga Khan Palace", description="A historic palace and memorial associated with India's independence movement.", category="Historical Site", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Sinhagad Fort", description="A hilltop fort with trails and views of the surrounding countryside.", category="Nature", rating=4.5, estimated_time_hours=4.0),
        PlaceModel(name="Raja Dinkar Kelkar Museum", description="A museum displaying a wide-ranging collection of Indian decorative arts and objects.", category="Cultural Site", rating=4.3, estimated_time_hours=2.0),
    ],
    "ahmedabad": [
        PlaceModel(name="Sabarmati Ashram", description="The former residence of Mahatma Gandhi and a museum about his life and work.", category="Historical Site", rating=4.6, estimated_time_hours=2.0),
        PlaceModel(name="Adalaj Stepwell", description="An ornate 15th-century stepwell with carved stone galleries.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Sidi Saiyyed Mosque", description="A historic mosque famous for its carved stone lattice windows.", category="Religious Site", rating=4.5, estimated_time_hours=1.0),
        PlaceModel(name="Kankaria Lake", description="A recreational lakefront with gardens, attractions, and walking paths.", category="Nature", rating=4.2, estimated_time_hours=2.5),
    ],
    "lucknow": [
        PlaceModel(name="Bara Imambara", description="An 18th-century complex known for its monumental hall and labyrinth.", category="Historical Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Chota Imambara", description="An ornate historic monument with decorative interiors and a reflecting pool.", category="Historical Site", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Rumi Darwaza", description="A monumental gateway and distinctive example of Awadhi architecture.", category="Landmark", rating=4.4, estimated_time_hours=1.0),
        PlaceModel(name="British Residency", description="Historic ruins and a museum documenting the 1857 uprising in Lucknow.", category="Historical Site", rating=4.4, estimated_time_hours=2.0),
    ],
    "bhubaneswar": [
        PlaceModel(name="Lingaraj Temple", description="A major Hindu temple and landmark of Kalinga architecture.", category="Religious Site", rating=4.6, estimated_time_hours=1.5),
        PlaceModel(name="Udayagiri and Khandagiri Caves", description="Ancient rock-cut caves with inscriptions and views over the city.", category="Historical Site", rating=4.5, estimated_time_hours=2.5),
        PlaceModel(name="Mukteshwar Temple", description="A 10th-century temple known for its carved gateway and stonework.", category="Religious Site", rating=4.5, estimated_time_hours=1.0),
        PlaceModel(name="Rajarani Temple", description="A historic sandstone temple set in landscaped grounds.", category="Historical Site", rating=4.4, estimated_time_hours=1.0),
    ],
    "guwahati": [
        PlaceModel(name="Kamakhya Temple", description="A major Hindu pilgrimage temple on Nilachal Hill.", category="Religious Site", rating=4.6, estimated_time_hours=2.5),
        PlaceModel(name="Umananda Temple", description="A historic Shiva temple on Peacock Island in the Brahmaputra River.", category="Religious Site", rating=4.4, estimated_time_hours=2.0),
        PlaceModel(name="Assam State Museum", description="A museum with collections on Assam's history, culture, and natural heritage.", category="Cultural Site", rating=4.2, estimated_time_hours=2.0),
        PlaceModel(name="Brahmaputra Riverfront", description="A riverside area for views of the Brahmaputra and sunset boat trips.", category="Nature", rating=4.3, estimated_time_hours=1.5),
    ],
    "srinagar": [
        PlaceModel(name="Dal Lake", description="A Himalayan lake known for shikara rides, houseboats, and mountain views.", category="Nature", rating=4.7, estimated_time_hours=2.5),
        PlaceModel(name="Mughal Gardens", description="Historic terraced gardens overlooking Dal Lake and the surrounding mountains.", category="Nature", rating=4.5, estimated_time_hours=2.5),
        PlaceModel(name="Shankaracharya Temple", description="A hilltop temple with panoramic views across Srinagar.", category="Religious Site", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Hazratbal Shrine", description="A prominent white-marble shrine on the banks of Dal Lake.", category="Religious Site", rating=4.5, estimated_time_hours=1.5),
    ],
    "shimla": [
        PlaceModel(name="The Ridge", description="A central open promenade with views of the surrounding mountains.", category="Landmark", rating=4.5, estimated_time_hours=1.5),
        PlaceModel(name="Mall Road", description="A pedestrian shopping street lined with cafés and colonial-era buildings.", category="Shopping", rating=4.4, estimated_time_hours=2.0),
        PlaceModel(name="Jakhu Temple", description="A hilltop Hanuman temple reached by a steep walk or local transport.", category="Religious Site", rating=4.4, estimated_time_hours=2.5),
        PlaceModel(name="Christ Church", description="A landmark neo-Gothic church overlooking The Ridge.", category="Historical Site", rating=4.4, estimated_time_hours=1.0),
    ],
    "darjeeling": [
        PlaceModel(name="Tiger Hill", description="A sunrise viewpoint with views of the Himalayan peaks on clear days.", category="Nature", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Darjeeling Himalayan Railway", description="A UNESCO-listed mountain railway known for its historic toy train.", category="Cultural Site", rating=4.6, estimated_time_hours=3.0),
        PlaceModel(name="Batasia Loop", description="A landscaped railway loop with a memorial and mountain views.", category="Landmark", rating=4.4, estimated_time_hours=1.0),
        PlaceModel(name="Himalayan Mountaineering Institute", description="A mountaineering museum and training institute near the zoo.", category="Cultural Site", rating=4.4, estimated_time_hours=2.0),
    ],
    "puducherry": [
        PlaceModel(name="Promenade Beach", description="A seafront promenade along the Bay of Bengal, popular for walks.", category="Beach", rating=4.4, estimated_time_hours=1.5),
        PlaceModel(name="French Quarter", description="A heritage district known for colonial-era streets and colorful buildings.", category="Cultural Site", rating=4.5, estimated_time_hours=2.0),
        PlaceModel(name="Sri Aurobindo Ashram", description="A spiritual community and meditation center in the city.", category="Religious Site", rating=4.4, estimated_time_hours=1.5),
        PlaceModel(name="Paradise Beach", description="A sandy beach reached by boat from Chunnambar Boat House.", category="Beach", rating=4.3, estimated_time_hours=3.0),
    ],
}


async def fetch_places(
        destination:str,
)->list[PlaceModel]:
    return PLACES_DATABASE.get(destination.lower(), [])