C - Customer (Mario Loescher)

R - Requirements Engineer (Danil Afanasev)

C: Hi!

R: Hi!

C: Thanks for meeting me, Daniel.

R: Thank you.

C: OK, so your questions are...

R: Food Delivery System. We need to clarify your needs.

C: OK!

1.  R: As we understand there should be two kinds of users: the customer
    > and the one who updates dishes.

> C: So, what's the question here?
>
> R: Should there be one admin who is responsible for updating dishes in
> all cafes or every cafe has its login?
>
> C: I would strongly prefer to have more than one administrator account
> (for future projects)
>
> R: In this case it's possible for one admin to manage different
> canteens.
>
> C: Yes. Idea is to have one "main" administrator who creates canteens
> \[profiles\]. The main "admin" can assign roles. For example, the
> "main" admin assigns a role to another admin to be the manager of all
> canteens in Innopolis. And somebody else will be the manager of some
> canteens in Kazan. But we want to stay flexible here.

2.  R: Could the customer schedule multiple orders at once?

> C: One order - one meal.
>
> R: If we make it possible to schedule for the whole week, should we
> provide a feature of copying all orders from one day or all orders
> from a previous week?
>
> C: We can do, but put it as a lower priority. It's not important, but
> it's nice to have.

3.  R: How is the order processed once a customer makes this order?

> C: You mean to the canteen itself?
>
> R: Yes.
>
> C: At the canteen we will have managers.

4.  R: Could we use any technology, like web, different frameworks, or
    > you have specific preferences?

> C: No, we have no system at the moment, so you are free to choose
> whatever you want. We just suppose it to work in the end.

5.  R: Are there any limitations like maximum amount of orders per user
    > per day?

> C: Well, three orders a day. You can't order more than one lunch.
> Because we have to integrate it with Innopolis system...
>
> R: Maybe a customer wants pizza at night.
>
> C: But the canteens are closed.
>
> R: There was not only canteens, there was also cafes planned. I guess
> the user should be able to order more than three dishes. The question
> is how many, 20, 50?
>
> C: The main problem here is we have to integrate the system. You can
> get a discount as a student, and you have your meal plan. We can't
> really do more than three dishes, at least discounted. You have to
> make sure you only get three dishes with discount, and everything else
> you have to pay the full price. Other than that, it will be really
> great to have this feature.

6.  R: A customer orders a pick up. What if a customer doesn't show up?
    > How do we process this situation?

> C: The dish will stay there as long as nobody takes it. If it's
> standing too long there, we might remove it. That's actually what
> canteen is doing.
>
> If you've missed your time, then you've missed it. So, be prepared or
> order a delivery to your home. Or ask somebody else to get it for you.
>
> For you it's just the order is in there, the order have been done in a
> canteen. We don't mind anything more.

7.  R: In the first document there is mentioned a few features. And I
    > want to know which ones are the most important, do we need to
    > implement 100% all of them. Delivery, picking up and updatable
    > menu.

> C: For the software there is no difference in process. But we only
> want to implement a time frame window when you will receive your food.
> Because if everyone selects an order at 6 o'clock, they will complain
> because food comes at 6:35. We have to keep some time frame.
>
> R: Some kind of a queue.
>
> C: Yeah. You will get your food between 6:00 and 6:15 for instance.
> But it would also be good if time frame is editable. Maybe it's not 15
> minutes, but maybe a half of an hour, depending on how many orders we
> have.

8.  R: Do we implement a payment feature?

> C: There has to be a payment system.
>
> R: I see difficulties here because...
>
> C: Because we have the meal plan already?
>
> R: Who gets the money?
>
> C: I get the money!
>
> R: Well, I doubt, because everything we do now... Innopolis University
> owns this software.
>
> C: Yeah, and then I assign it to Innopolis of course.
>
> R: To implement a payment feature we need a lawyers team, which we
> don't have.
>
> C: Why do you need a lawyers team for payments system?
>
> R: How to process money, how to make everything legal...
>
> C: If you have doubt, we can move this down in priority. We'll have
> the most important payment system, it's cash. It's probably the
> easiest way to implement this. And if we have time later on we can
> still create it. But I doubt we need a lawyer. It's not that important
> as long as it's in Innopolis. Just keep in mind the software has to be
> maintainable, so we can add it in the future, if we want.

9.  R: Do we provide templates? Templates for orders, templates for
    > admin with dishes.

> C: So, you can select something having a preconfigured menu?
>
> R: Yeah.
>
> C: Yes, it's actually stated in requirements, which is written so far.

10. R: Should customers be able to leave comments about a particular
    > canteen? And grade it. Like, with stars.

> C: Yeah, I can imagine. I didn't think about this possibility. It's
> nice to have this feature, but please put it down in priority.
>
> I think, we have to discuss the priorities later on.
>
> R: The same goes for particular dishes?
>
> C: No, not for the dishes itself.
>
> R: We shouldn't grade dishes. 5 stars, 3 stars?
>
> C: OK, we could actually take this grades. You can grade the food
> itself and calculate the grade for a canteen.
>
> R: Nice!
>
> C: So, you only grade food that you've got. And the canteen is graded
> automatically.
>
> But the problem here is now: do you have to order before \[to be able
> to grade\]? Because a lot of people are just going over there and just
> eat. They don't order \[in our app\]. So, it's a nice feature, but how
> do we work with these people? We can't just let people vote as often
> as they want. Maybe once a day per smartphone or whatever. If people
> hate one of the canteens, they just vote it down all the time.
>
> So, it's a nice feature, but it's not that important, especially
> because we have this trouble. I guess, I have to think about it with
> my team.

11. R: One more question related to this topic. Should a user be able to
    > write a complaint to a cafe administrator?

> C: Yes, why not?

12. R: And in this case the admin has an ability to write a response to
    > the customer.

> C: Yeah.

13. R: Should we somehow manage in our application the number of
    > prepared items of a dish? When it's out, we do not let a user
    > order this dish anymore.

> C: That's impossible for us.
>
> R: Counting will be difficult. Maybe just a button, like "It's over.
> Don't order this anymore"?
>
> C: Yeah, but people have already ordered it. If it's out in a canteen
> and somebody has already ordered it, we have to make sure in the
> canteen that the order is completed, and...
>
> R: So, we will not think about it.
>
> C: No. It's too much of a hassle here. But it's a good point: what do
> we do if food is out if it's been ordered. But still we just have
> orders, it should work for a manager.

14. R: Do we need Russian localization?

> C: Russian and English. But English is the most important.

15. R: Do we plan our system to be extendible in the future: for more
    > cities, for more universities?

> C: Yeah, we've already discussed it.
>
> R: Yes.

16. R: Anything else you wanted to add?

> C: No. I have no ideas left.
>
> R: Thank you very much.
>
> C: You're welcome. Thank you.
