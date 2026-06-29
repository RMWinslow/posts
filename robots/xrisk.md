

In ["If No One Builds It, Everyone Dies"](https://nicholasdecker.substack.com/p/why-we-should-be-less-concerned-about)
Nicholas Decker argues that it's ethical to risk human extinction 
by developing a powerful technology like AGI,[^AGI] 
since that tech would reduce the risk of death and extinction from other causes. 


The bit that nerd-sniped me:

> If you are a utilitarian, whether or not we should accept the risk is simply a matter of what parameters you believe about extinction risk, the future flow utility of humanity living without AGI, and the future utility of humans with AGI.

[^AGI]: AGI: Artifical General Intelligence. Super duper intelligent AI that's good at everything.


So this is a silly exercise, but sure, let's take a moment to think through those parameters.


## Extinction Risk Only

For simplicity, let's assume you want humans and human civilization to continue to exist as we know it, and you don't particularly care about the details, or even whether you're around to see it.[^posterity]

[^posterity]: The latter isn't even a particularly weird assumption. People sacrifice for posterity all the time, and it makes perfect sense within all sorts of preference frameworks. I mean, when people say that having kids is a form of immortality, it isn't *just* a metaphor.

The parameters are as follows:

- You have $u$ units of utility for each year humanity endures,
- you discount the future at rate $\delta$,
- and there's a risk $x$ that humanity goes extinct or otherwise ceases to endure.

Your expected utility looks like this:

$$
U = \sum_{t=0}^\infty \left(1-x \over 1+\delta \right)^t \cdot u
=
\frac{(1+\delta)u}{\delta+x}
$$

Now let's say AGI does two things:

- It instantly destroys us with probability $p$
- but it also adjusts the ongoing extinction risk from $x$ to $q\cdot x$.

If you press the AGI button, your expected utility will be:

$$
U_{agi} = \sum_{t=0}^\infty \left(1-q\cdot x \over 1+\delta \right)^t \cdot u
=
(1-p)\frac{(1+\delta)u}{\delta+qx}
$$

### Should You Turn On The AGI?

If we're expected utility maximizers, 
then we should push the AGI button iff $U_{agi} > U$, which is true when:

$$
p < \frac{(1-q)x}{\delta +x}
$$

<!-- Same ultimate condition in continuous time. Just each utility lacks the (1-delta) factor in the numerator. -->



Let's be generous to the robot, and assume that AGI completely removes all other extinction risks, allowing humanity to endure in perpetuity. 
($q=0$). 

And let's use the "standard" 2% discount rate for $\delta$.

What number should we use for the non-ai extinction risk?
Based on our survival as a species so far, [the "background rate" of human extinction is probably much less than 10e-4](https://www.nature.com/articles/s41598-019-47540-7), 
but modern times allow for modern means of extinction, and it isn't *just* total extinction that we care about,
but any sort of permanent end to human civilization.
In *The Precipice* Toby Ord gives [estimates for various existential risks](https://forum.effectivealtruism.org/posts/Z5KZ2cui8WDjyF6gJ/some-thoughts-on-toby-ord-s-existential-risk-estimates). He warns us not to take the numbers too seriously, but he estimates a 1/6 overall change of catastrophe this century, and 1/10 from AI in particular. If the AI and non-AI risks are independent, that gives a 1/13 risk of non-ai extinction this century, and about 1/1300 per year.

$$
p < \frac{1/1300}{1/50 + 1/1300} = \frac{1}{27} \approx 3.7\%
$$

So don't summon the machine-god unless there's less than a one-in-30 chance it destroys the world as we know it? Sure. Sounds reasonable to me. 


