# MemoryTrunk
MemoryTrunk is a database-driven web application built upon the Django framework. It is based upon the idea of "Crowdsourcing Life Experience", i.e. learning from other people's mistakes/successes. It is built with a mindfulness for personal enrichment, facilitating the ability to identify influences and implement processes which contribute to a higher quality of life.


### Memory 
When a user experiences an important life event, they may record the details of said event as a Memory object in the MemoryTrunk database. This may be for the user's own sake, to remember it later, or because they believe other users could gain valuable information from it that will help them go through similar life events.

When creating a Memory, user's rank the happiness it gives them from 0-10. This is so they may take advantage of MemoryTrunk's "Happy Memories" interface, which reminds user's of all the memories that have brought them happiness over the years.


### Tip
When a user believes they have a piece of advice that would be valuable for them to remember, or for other users to see, then they may record it as a Tip object in the MemoryTrunk database. Tips can be liked by users, both to save them to that user's collection and to show support for the usefulness of said Tip. Tips tend to have a specific goal in mind (unlike Perspectives, which tend to offer more generalized views on life or a situation).


### Perspective
When a user finds a particular view on life - or a situation - to be either enriching or useful, they may save that view as a Perspective object in the MemoryTrunk database. A Perspective is generally wider in scope than a Tip, and may offer views such as "Worrying only makes a situation worse" or "Sometimes the book with the scariest cover becomes your best friend". While generally less direct than a Tip, Perspectives have the ability to offer users a way of looking at things, or doing things, that may significantly improve their quality of life. A Tip tends to be more of a "how to" guide, while Perspectives trend towards philosophical approaches to life.


***
##### Going Forward/Installation
MemoryTrunk is not currently hosted on a server. However, that should change within a week. If you wish to use this program in the meantime, you may clone it down to your machine. 

MemoryTrunk utilizes Python version 3.6.0 and Django version 1.10.5

After installing these dependencies, you should be able to run the program from a terminal window in the Django project's root directory by running `$ python manage.py runserver`


