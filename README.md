# poetry-ai
This project was created as an exploration of the GTP-3 model and the potential for AI-generated poetry. It uses a dataset collected from the Poetry Foundation: a random assortment of complete and partial poems is selected from said dataset to give the model an idea of what kind of text and what subject matters we would like for it to produce. Playing around with the API, I have discovered that by feeding the model a specific author's work (say, Emily Dickinson, who has a very distinctive voice), the model will produce novel poems "authored" by said poet, making use not just of their style, but also identifying and reproducing their themes as well as extending metaphors they used in their poems. 

The poems are not always perfect simulacra of poetry that would make a poet proud or poetry that might make it through the usual filters of quality required to be published (they frequently come out sounding like they could have used the assistance of a good editor), but it is quite significant that the poetry produced simulates specific styles successfully. In fact, I think the model may be better at this than most human writers; if copying style were more manageable, we would have had far fewer authors known for their very singular, inimitable talents like Shakespeare or Marcel Proust, yet GPT-3 is able to produce text that sounds like it comes straight from one of their masterpieces, the only caveat is that the produced text is occasionally wholly non-sensical.

The extension and creation of metaphors are an incredible facet of the model, as not only is the model able to identify metaphors, but it works with the conceptual connections and builds them out along a line of logic that seems, for lack of a better word, soft: it seems intuitive that a computer would struggle to make connections between disparate concepts, but not only is it able to make seemingly novel bonds, but it has a sense of conceptual proximity, making new connections just a step over from previous bonds.

[INSERT EXAMPLES OF PRODUCED TEXT AND COMPARISONS TO ORIGINAL AUTHORS]

I used Tweepy to create a Twitter bot that automatically tweets poems it has produced. I plan on working with the code further to enable the bot to automatically respond to tweets using the GPT-3 API to generate its responses. 

There are potential applications for generative songwriting here as well.
