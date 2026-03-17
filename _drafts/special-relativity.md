---
title: "Special Relativity"
parent: science
math: katex
---

# A slightly simplified explanation of special relativity.

This page is an exeriment with explanatory writing style. 

It's essentially a copy of ["On The Electrodynamics Of Moving Bodies"](http://www.fourmilab.ch/etexts/einstein/specrel/specrel.pdf), which Einstein wrote back in 1905. 
This page has the same content as the original, and is presented in the same order.
But the maths is trimmed, the definitions are less rigourous, 
and there's a lot of emojis in place of greek letters.

https://en.wikisource.org/wiki/Translation:On_the_Electrodynamics_of_Moving_Bodies

## Main Idea

The earth and solar system are whizzing about in space. 
People used to think that since the earth is moving, it must be moving *through* something that's *still.*
Simple idea. Turns out it doesn't work that way.
There were [some big experiments](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment) which tried to measure the still stuff, and couldn't find any evidence it exists.

So there's no such thing as "absolute rest". Where do we go from here? 

Einstein starts by assuming the following two things:
1. **The Principle of Relativity:** Light and electromagnetism follow the same laws in every frame of reference[^1]. That is, your laptop will still work the same on a moving train.
2. **Constant speed of light:** Light always moves at some specific speed we call "$c$", and this speed doesn't change depending on the motion of the lightsource. That is, the light coming out of the headlights of a moving car doesn't go any faster than the light coming out of a parked car. 

[^1]: This only applies to "inertial" frames of references. 
    That is, if the laws of physics apply to some coordinate system, 
    then the same laws apply to a second coordinate system 
    which is sliding past the first at a constant velocity. 

[^2]: Light actually moves at $c$ in a *vacuum*, 
    and moves more slowly through other mediums. 
    But we'll ignore this for now. 
    The important bit is just that light doesn't go faster when its source is moving.

<aside markdown="block">
Light actually moves at $c$ in a vacuum, 
and moves more slowly through other mediums. 
But we'll ignore this for now. 
The important bit is just that light doesn't go faster when its source is moving.
</aside>

With these two starting assumptions, we can describe motion in a way that doesn't require some universal objective notion of stillness. But doing so has some weird implications.

*(Note that Einstein isn't providing evidence of the above assumptions. There were already experiments showing those to be true. What Einstein does is explain how these assumptions fit together, and the implications that these assumptions have.)*


## Part 1. Stuff Moving About

### What does it mean for events to happen at the same time?

We're trying to carefully describe what movement is. 
To do that, we first need to carefully think about *time* and *position*.
What do these concepts even mean?

First we need to define time. That's easy. The time is whatever my watch ⌚ says it is. If a dog "barks at 7:00", it means that when the dog barked, my watch also read `7:00`.

This gets tricky over long distances. 
(If you've ever been in a thunderstorm, you know that there's a delay before you hear the thunder.)
So let's say my friend has another clock ⏰ which is in sync with my watch. 
And we'll say that the time when something happens is based off of the clock right next to it.

#### Example 1

Alan's dog barks. He looks at his watch. It says `7:00`.
Betty's cat meows. She looks at her clock. It says `7:00`. 
If her clock and his watch are in sync, then we can say the bark and the meow happened "at the same time". 

Simple, right?

Here's a slightly more complicated example:

#### Example 2

Alan's standing at a distance $d$ away from Betty. 
He turns on his flashlight at some time we'll label $⌚_1$. 
The light goes to Betty and hits her mirror at time $⏰_2$. 
Finally, the light bounces back to Alan's eyes at time $⌚_3$. 
(Remember, we measure the time of an event by using the clock that's right next to it.)

![Alan and Betty doing science.](lightbounce.svg)

The **speed of light is constant**. And speed is just distance over time. 
So two things should happen in this example:

- First, it should take the same amount of time for the light to go each way. 
  If our clocks are in sync, then 
  
  $$⌚_3 - ⏰_2 = ⏰_2 - ⌚_1 = \text{The time it takes the light to travel distance d.}$$
- Second, Alan should be able to measure the speed of light by timing how long it takes for the light to bounce back:
  
  $$\frac{2\cdot d}{⌚_3 - ⌚_1} = c$$

  $$\frac{\text{Distance the light travels.}}{\text{The time it takes.}} = \text{Speed of Light}$$
  
  and this should always give the same speed. 

### Woops. Time is now relative. 

Let's measure a train. How long is it?

Easy: However long the measuring stick says it is! 

Let's measure the train while it's still, and call this length $📏_{still}$

Things get a bit trickier when the train is in motion. 
It would be really difficult and dangerous to put our measuring stick next to a moving train, so now we have two options.

First option is to give the measuring stick to someone riding the the train,
and ask them to measure it while it's moving. Call this length $📏_{onboard}$.

Or we could take a picture of the train as it whizzes past, 
mark the position of the front and back of the train at some specific point in time,
and then measure the distance between those two points on the track.
Call this length $📏_{outside}$.

![Three different ways to measure a train.](trains-length.svg)

So now we have three different measurements for the length of the train. 
We used the same train and the same measuring stick each time, 
so we'd expect that we'll get the same length, right?

Our **Principle of Relativity** assumption says that if the train is moving at a constant velocity, 
then the experience of a moving person measuring the moving train should be exactly the same
as a still person measuring the still train. So

$$📏_{still} = 📏_{onboard}$$

But we don't know for sure whether $📏_{onboard}$ is also the same. (And we'll see in a later section that it isn't.)

#### Example 3:

Put Alan and Betty inside the moving train.

1. Alan turns on his flashlight at time $⌚_1$. 
2. The light goes forwards, in the same direction as the train, and hits Betty's mirror at time $⏰_2$. 
3. The light bounces backwards and travels in the opposite direction, hitting Alan's eyes at time $⌚_3$. 

There's also a third person, Carl, watching from alongside the tracks. He has his own clock.

![An image showing the three people monitoring this experiment.](train-shift.svg)

What does Carl see? 
The **constant speed of light** assumption says that
the light going forward from Alan's flashlight should be going the same speed 
as the light bouncing backwards from Betty's mirror.
Because the train is also moving, 
the light will take longer to go from flashlight to mirror
than it will to go from the mirror back to Alan.

Therefore, if both Alan's and Betty's clocks are synchronized with Carl's clock, 
Carl with observe that

$$⌚_3 - ⏰_2 = \frac{📏_{outside}}{c+v} < \frac{📏_{outside}}{c-v} = ⏰_2 - ⌚_1$$

where $v$ is the speed of the train and $c$ is the speed of light.

What do Alan and Betty see?
The **Principle of Relativity** assumption says that
their experiment should work exactly like the one from Example 2.
If their clocks are in sync with each other, then 

$$⌚_3 - ⏰_2 = \frac{📏_{onboard}}{c} = ⏰_2 - ⌚_1$$

Uh oh. Do you see the problem here?
These two equations can't both be true.
So if the clocks look in sync to Carl, then they can't look in sync to Alan and Betty.
And vice versa. 

This means that it's not just motion that's relative. 
Even our concept of "things happening at the same time" depends on the frame of reference.
This is the first weird consequence of our assumptions[^3].

[^3]: We might then conclude that this is *too* weird; one of our assumptions must be wrong.
    Maybe the light comes out of Alan's flashlight faster on a moving train.
    Or maybe the Principle of Relativity just isn't that strong. 
    But again, Einstein isn't providing evidence of these two assumptions;
    there were already several big experiments showing them both to be true.
    What Einstein is doing is *starting* with these assumptions, and then making predictions.
    And as it turns out, the predictions are true. [Time really is relative](http://www.astronomy.ohio-state.edu/~pogge/Ast162/Unit5/gps.html).
    It's just that we're usually not moving fast enough to notice.








