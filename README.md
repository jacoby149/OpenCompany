# OpenCompany
A convection oven for aspiring code monsters 😎💯👨‍💻



## What is OpenCompany?

A system to build practical experience after Computer Science school / boot camp.

A system that companies can attach to their open source repos to issue stock and compensation to developers and mentors.

It is a community of people developing software for Company Stock. 

It is a community of mentors teaching students with merit based certifications.



## Why? 

There is a missing gap between Computer Science School / Bootcamp and landing the first paid internship.

OpenCompany is a system that allows people to contribute to open source projects for stock compensation, and build their resumes.



Open Company creates a metaphorical karate dojo of code, with people of higher ranks mentoring the lower ranks.

Build practical coding experience with a mentor.

Hit successfully merged commit count milestones in order to rise in the ranks.

When achieving milestones, you pay mentors + the Open Source Company for promotion, similar to the black belt test fee in a karate dojo.

On promotion, you receive stock options of said Open Source Company

[Totally Configurable !!]

[ SEE api\app\rank.py ] 



The fee serves as :

- a payment for mentees to appreciate the work of mentors/teachers.
- compensation to the company for the creation of a practical learning opportunity with a mentor.

The Stock serves as :

* An incentive to the mentees and mentors to develop code and mentor for the Open Source Company.



## A Little More Detail



**Mentor Rewards / Payment** : majority of certification fees [ 55% - 85% based on rank] goes back to pay the mentors/teachers. 

The rest goes back to the configured Delaware C. Corp.

[Totally Configurable!!!]

[ SEE api\app\rank.py ] 



**Developer Rewards / Payment :** promotion / rank increase is rewarded with : 

- 100 - 1,600 Shares of Corporate Stock, [Totally Configurable!!!]
- Access to exclusive discord chat for your dojo rank.
- More opportunity for leadership in the community.
- A larger portion of mentor fees.



**Clarification** : All Developers are eligible to be mentors after ranking up once! The only criteria to mentor is that you be a rank above your mentees. On mentee promotion, the mentee is required to put in a name of ONE mentor. Mentees choose the mentors, and can string you on. It is not the other way around.



## How to Run OpenCompany Locally 

1. get github api keys to put in the settings.py file.
2. copy the settings_example.py, and configure it to a repo of choice, user, and repo name. [TODO support multiple repos.]
3. Install Docker, and run the command :

```
docker-compose up --build
```

