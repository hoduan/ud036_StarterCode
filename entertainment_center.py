# -*- coding: utf-8 -*-

import media
import os
import fresh_tomatoes

DIR = os.getcwd()

titanic = media.Movie(
    "Titanic",
    "Leonardo DiCaprio and Oscar-nominatee Kate Winslet light up the" +
    " screen as Jack and Rose, the young lovers who find one another" +
    " on the maiden voyage of the 'unsinkable' R.M.S. Titanic. But " +
    "when the doomed luxury liner collides with an iceberg in the " +
    "frigid North Atlantic, their passionate love affair becomes a " +
    "thrilling race for survival.",
	DIR + "/poster/" + "titanic_poster.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
    )

zootopia = media.Movie(
    "Zootopia",
    "The modern mammal metropolis of Zootopia is a city like no other. " +
    "Comprised of habitat neighborhoods like ritzy Sahara Square and " +
    "frigid Tundratown, it’s a melting pot where animals from every " +
    "environment live together—a place where no matter what you are, " +
    "from the biggest elephant to the smallest shrew, you can be " +
    "anything. But when rookie Officer Judy Hopps (voice of Ginnifer " +
    "Goodwin) arrives, she discovers that being the first bunny on a " +
    "police force of big, tough animals isn’t so easy. Determined to " +
    "prove herself, she jumps at the opportunity to crack a case, " +
    "even if it means partnering with a fast-talking, scam-artist fox, " +
    "Nick Wilde voice of Jason Bateman), to solve the mystery.",
    DIR + "/poster/" + "zootopia_poster.jpg",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM"
    )

moonlight = media.Movie(
    "Moonlight",
    "Free Fire, A Ghost Story, How to Talk to Girls at Parties." +
    "It Comes at Night, Woodshock, Slice, Good Time",
    DIR + "/poster/" + "moonlight_poster.jpg",
    "https://www.youtube.com/watch?v=9NJj12tJzqc"
    )

jungle_book = media.Movie(
    "The Junge Book",
    "'The Jungle Book' seamlessly blends live-action with photorealistic" +
    "CGI animals and environments, using up-to-the-minute technology " +
    "and storytelling techniques to immerse audiences in an enchanting " +
    "and lush world",
    DIR + "/poster/" + "jungle_book_poster.jpg",
    "https://www.youtube.com/watch?v=HcgJRQWxKnw"
    )

la_la_land = media.Movie(
    "La La Land",
    "LA LA LAND tells the story of Mia [Emma Stone], an aspiring actress, " +
    "and Sebastian[Ryan Gosling], a dedicated jazz musician, who are " +
    "struggling to make ends meet in a city known for crushing hopes " +
    "and breaking hearts. Set in modern day Los Angeles, this original " +
    "musical about everyday life explores the joy and pain of " +
    "pursuing your dreams",
    DIR + "/poster/" + "lalaland_poster.jpg",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8"
    )

inside_out = media.Movie(
    "Inside Out",
    "Growing up can be a bumpy road, and its no exception for Riley, " +
    "who is uprooted from her Midwest life when her father starts a " +
    "new job in San Francisco. Like all of us, Riley is guided by her " +
    "emotions: Joy, Fear, Anger, Disgust and Sadness. The emotions live " +
    "in Headquarters, the control center inside Riley’s mind, where they " +
    "help advise her through everyday life. As Riley and her emotions " +
    "struggle to adjust to a new life in San Francisco, turmoil ensues in " +
    "Headquarters. Although Joy, Riley's main and most important emotion, " +
    "tries to keep things positive, the emotions conflict on how best to " +
    "navigate a new city, house and school.",
    DIR + "/poster/" + "inside_out_poster.jpg",
    "https://www.youtube.com/watch?v=_MC3XuMvsDI"
    )

movies = [titanic, zootopia, moonlight, jungle_book, la_la_land, inside_out]

# open movies page in the browser
fresh_tomatoes.open_movies_page(movies)
