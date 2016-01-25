title: First attempts at Lifelogging with Twitter
date: 2013-09-17
tags: lifelogging
status: draft

Around March 2013, I began tracking the food that I eat, logging workouts, and taking miscellaneous personal notes with Twitter.  At first, my goals were simple: start tracking as much as possible and then analyze it later.  Over time, I settled on tracking food consumption, workouts, and mood.  My hypothesis (biases aside) is that the food that I eat and the exercise that I do has a measurable effect on my quality of life.

Before I settled on logging with Twitter, I shopped around for other tracking apps for my Android phone, but wasn't satisfied with how the app addressed my use case.  Particularly for food: what if the food I eat isn't in the database?  How long does it take me to open the app, type in the food, use the drop-down, select a quantity and units?  I contemplated writing my own Android app to ease these concerns, but fortunately settled on a stupidly simple semi-structured text solution using Twitter.

I learned of a Google Apps Script that I could run, free of charge, on a daily timer, to copy my Twitter archive to Google Drive.  With all my data in one places, I could parse the data with python into rows keyed by timestamp and containing text for tokenizing and analysis.

At first, I had doubts that I could habitually track all of my food without developing some neuroses.  The data, actually, was straightforward to collect and had some positive side effects on my behavior.  The practice helped be much more mindful about the food that I eat, what ingredients are in my food, how that food makes me feel, etc.  I'd find myself declining to eat something because it wasn't worth the effort to track it.

When logging food, I use an abbreviation for the particular food that I'm eating that's defined in a text file.  That abbreviation is mapped to entries in the USDA National Nutrient Database, a giant table with >8,000 rows of foods and measurements of 140 nutrients found in those foods, including macronutrients, individual fatty acids, individual amino acids, vitamins, and minerals.

The parsing-and-analysis step is an ongoing hack-fest, but I will be committing over on Github.  My new revised goal for this project is to build a (personal) platform for logging everything possible with semi-structured text.  I don't intend for this code to be meaningful to anyone but me, but maybe it will enable some interesting analyses to share!
