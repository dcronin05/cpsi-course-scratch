# Transcript: Programming 2: Module 1 (Lecture Slides Part B)

[00:00] Whoops.
[00:02] I should go record this and do a one
[00:04] take, but I found out that doing a tick
[00:07] mark is what my hotkey is for starting
[00:09] and stopping recording. So, whoops.
[00:11] Okay, so I'm back. So, um
[00:15] so anyways, uh there is a thing you can
[00:19] do to like whenever you're typing in
[00:21] really big numbers to separate um the
[00:24] digits in C++. Let me look that up. C++
[00:30] uh digit
[00:32] separate separ separator
[00:37] you can use a single quote. Okay, so
[00:40] let's do that. Um sometimes when you're
[00:43] typing in really big numbers it's nice
[00:44] to like make it where you can read them
[00:46] a little easier. So here is uh two
[00:49] billion
[00:50] and uh I'll print out xoop.
[00:53] All right. And then I'll print out x + x
[00:58] and we will see what happens.
[01:01] All right,
[01:06] that's million. I Okay. Oh, I changed to
[01:09] 56. Okay. And I needed to do billion. So
[01:14] I can do I know what a billion is.
[01:17] So two billion plus two billion is
[01:22] 29 million.
[01:24] That's because you have overflow. Once
[01:27] it goes off the biggest number, it comes
[01:29] around to the smallest number and keeps
[01:30] on cycling like this. Doesn't throw an
[01:33] air. It's one of the biggest. It's it's
[01:35] a foot gun that uh C++ has. You don't
[01:39] know when it happens because it doesn't
[01:40] throw an error. Like you got to be very
[01:43] careful. So if I change this from int to
[01:46] long, bam, I would then not have a
[01:50] problem. So, um, you wouldn't offend me
[01:53] if you just always use long and never
[01:55] use ins. So, that probably would
[01:57] actually solve the the problem. There
[01:59] are a few small little issues that you
[02:01] might come across by doing this, but um,
[02:04] you're not going to run out of memory
[02:06] for things you're going to do in this
[02:07] class. So, um, we got int, we got longs,
[02:10] we got floats, and doubles. Floats and
[02:12] doubles are whenever you want to have u
[02:14] you want to have something with a
[02:15] decimal place. So, uh, let's let's do
[02:18] something like that. There you go.
[02:21] That's a That's a double. Doubles have
[02:24] about four uh about 15 digits of
[02:27] precision and floats have about seven.
[02:30] And they can store numbers as big and
[02:32] small as you'd ever need. Right? These
[02:34] these are astronomically big and and
[02:36] microscopically small. Um that's float.
[02:40] And then and then we go way beyond that
[02:43] for double. So, um you can you can do
[02:45] anything you want practically with a
[02:47] double, you know, like
[02:53] the these these are I can't stress how
[02:56] ridiculously precise and and good these
[02:59] are. Um like they can't you you actually
[03:03] can't represent numbers exactly. Like
[03:05] for instance, if I try to represent 0.1
[03:08] um the computer is actually storing
[03:09] everything in base two. So it's like
[03:11] 0.100000000001.
[03:14] It's like off in like the 15th 16th
[03:17] decimal place. And um but that is such a
[03:22] small problem that in practice it
[03:25] doesn't actually matter. It only it's
[03:26] only going to mess you up if you you use
[03:28] like a strict like is this equal is this
[03:30] equal to 0.1
[03:32] um issue. So you just have to check
[03:35] whenever you're checking equality. You
[03:36] never can be like 100% sure with a
[03:38] double. But like as far as like getting
[03:41] really close to the values and doing
[03:43] calculations, these are great. And on
[03:45] 64-bit machines, doubles are are just as
[03:49] fast as floats. And the same thing for
[03:52] long. Uh longs can calculate just as
[03:54] fast as ins because we have 64-bit
[03:56] machines. We can fit all we can do all
[03:59] the the the calculations for those
[04:01] things in in one CPU. Well, multiple CPU
[04:04] cycles and for some things like
[04:06] multiplication, but they they happen
[04:07] just as fast. There's really no
[04:09] performance hit. The only thing that
[04:12] hurts is you use more memory when you're
[04:14] using a long. A long uses a bytes and
[04:16] double uses a bytes. So you're using a
[04:18] little bit more memory, but I mean we
[04:20] have gigabytes of memory. So you could
[04:22] have literally billions of these things.
[04:24] Probably not going to happen in your
[04:25] rises programs right away.
[04:28] All right. So you can convert uh you can
[04:31] convert data. What are we trying to say
[04:34] here? There is different types of data.
[04:36] there's signed and unsigned data. Um,
[04:39] you can uh I'm not going to do it, but
[04:41] you can say unsigned int. And so this
[04:45] will be a an int that can only be
[04:47] positive numbers and can't be negative
[04:50] numbers
[04:52] that can cause let's actually just do a
[04:54] little example here. We'll do one here
[05:01] and I'll just say something simple like
[05:03] y - one or minus two
[05:09] and it goes to a really big number
[05:11] because it wraps around and instead of
[05:15] unsigned ants going from negative -2
[05:17] billion to positive 2 billion they go
[05:18] from 0 to 4 billion. So here you can see
[05:20] as I go off the bottom it goes up to the
[05:23] top. This can cause all sorts of
[05:25] problems obviously and the overflow
[05:27] happens a lot easier because you know
[05:29] you're bumping up against zero which
[05:31] where the overflow happens. So in
[05:33] general just don't use unsigned
[05:37] it just causes you heartache. So if I
[05:39] run this again we can get negative one
[05:41] like you expect. You do lose some range
[05:44] but you know if we didn't have enough
[05:45] range we just pop it up to long right.
[05:52] All right. So that's all I want to talk
[05:54] about that platform dependencies.
[05:57] Okay. So if I go back here, these are
[05:59] the sizes that they are typically on a
[06:03] PC that's running like Linux, Mac,
[06:06] Windows, but there are other platforms
[06:09] like microcontrollers
[06:11] that have different CPUs.
[06:14] They might be 8bit, they might be 16
[06:16] bit. C++ is like wildly flexible and
[06:19] very old and being in used in all sorts
[06:22] of uh of very low-level very um very
[06:26] low-level hardware.
[06:29] So sometimes an int might be one bite
[06:31] maybe maybe two bytes. It these things
[06:34] are are different depending on what
[06:36] you're compiling for what your compiler
[06:39] is what your platform is. These are all
[06:42] just um just you know you know the
[06:45] standard um you would think that they
[06:47] should be standardized and there are
[06:48] ways to like pin them but in practice
[06:51] don't worry about this um once you get
[06:54] to programming on a system that where it
[06:56] matters you'll probably be aware that
[06:58] this is a potential issue but for the
[07:00] most part you can roughly count on these
[07:02] things but you can always check you can
[07:06] always check there's a function called
[07:08] uh size of let me see So, I can just do
[07:12] I'm not exactly sure how I do it, but
[07:15] the size of Can I just throw an int
[07:18] here? What's the size of an int?
[07:22] It's four bytes. Check that out. And
[07:25] what's the size of a long?
[07:30] It's going to say eight bytes. And
[07:33] what's the size of?
[07:36] There's a thing called a long long,
[07:37] which is really just a long. So, it's
[07:39] just like saying long long saying long a
[07:42] lot. So, if you like writing long twice
[07:44] in a row, that's fun. Um, on some
[07:47] systems it could go up to 12 or 16, by
[07:49] the way, but not on this system and not
[07:51] on most systems. So, long long is
[07:53] usually just a waste. Anyway, so you can
[07:56] check in on the size of things and you
[07:58] can change your code to to behave
[08:00] differently depending on what that is if
[08:03] you want. Um,
[08:07] all right. So we got different sizes. We
[08:10] got the size of operator. You can also
[08:12] put a variable inside there instead of a
[08:14] type. And you can convert between types
[08:16] if you want to. Um you can do lots of
[08:19] conversion between types with you know
[08:21] sometimes obvious or not. So you can do
[08:24] implicit conversion. So I'll just say
[08:26] double A is equal to
[08:30] um
[08:31] equal to Y. So this is going to just
[08:34] take the int
[08:37] and just put it in a double. That's kind
[08:40] of a a widening of restrictions. And so
[08:43] it's less restricted. So it'll just do
[08:45] it. The the computer's okay just letting
[08:47] you let it happen. So you can go from a
[08:50] bool
[08:51] to an int to
[08:56] a
[08:58] float to a double. Anyways, you can you
[09:01] can you can go down that chain and and
[09:04] just get in more more and more or less
[09:07] and less restricted. If you want to go
[09:09] the other way, you want to go from like
[09:10] a double to an int, you're going to have
[09:12] to you're going to have to force it. So,
[09:15] let's say I want int B to be um to be a
[09:19] Z. Okay. And I'm going to try to print B
[09:22] here. So, um what does it mean to turn
[09:25] that double to it? Well, typically it's
[09:28] going to karate chop off the decimal
[09:30] point. So, we should get 23 here. Uh, we
[09:34] have all sorts of issues.
[09:38] All right. It says warning narrowing
[09:41] conversion and we're missing a semicolon
[09:45] um somewhere right there. All right. So,
[09:49] we're down to a warning and it does run.
[09:53] Um, but you can make this where the
[09:55] warnings don't um
[09:58] um the warnings stop you from compiling.
[10:02] You can you can throw a flag whenever
[10:04] you're you're compiling things. All
[10:05] right. Anyways, how do you how do you
[10:07] handle this? You can say static
[10:09] a cast and you can cast this to whatever
[10:13] thing you want. In this case, an int.
[10:16] And there we go. Syntax a little weird,
[10:18] but that's how you cast.
[10:22] You just slot in whatever here.
[10:24] Basically, you're calling your shot.
[10:25] Like, I know that this is going uh the
[10:28] wrong direction. Um, but I want to do it
[10:31] anyways and it'll let you. All right.
[10:37] Okay. We already talked about output.
[10:39] You can do we already talked about
[10:41] inline. Um, but you can get character
[10:43] inputs. Let's clean this all up.
[10:48] All right. So, let's make do a simple
[10:50] program. I want to ask for somebody for
[10:52] their age and then I want to tell them
[10:53] what year they were born maybe. So, um
[10:57] I'm going to get a variable called age.
[10:59] I don't know what it is yet. I'm going
[11:00] to ask the user. So, um I could ask the
[11:04] user with this character input stream. I
[11:06] can try to extract an age from them. And
[11:11] I'm going to run this.
[11:13] So, what it's going to do here, it's
[11:15] going to wait for me to type something
[11:16] in the keyboard. And then it's going to
[11:17] go on once I type it in. And whatever I
[11:19] type in is going to get fed in to um
[11:23] this age variable that I have here. Um
[11:26] but just like just you know you need to
[11:29] prompt them. You need to tell them what
[11:30] you expect otherwise they won't know
[11:32] what to do. So we're going to use a
[11:34] character output stream to say hey give
[11:36] me your age.
[11:38] Usually I put a space here. Usually I
[11:40] don't put a new line character so they
[11:41] can type on the same line. And let's
[11:44] actually go do something here.
[11:49] You were born in
[11:54] um
[11:58] blank
[12:02] or
[12:05] blank.
[12:11] All right. So, we need to figure out the
[12:13] blanks. Um let's do a year is going to
[12:17] equal something
[12:19] and this will be year
[12:22] or year + one or the other way around.
[12:24] Okay. So it is currently 2026
[12:30] and so if we subtract the age
[12:36] and it's after their birthday
[12:39] that'll be right. If it's the before the
[12:41] birthday, it'll be off by one.
[12:49] All right. Um
[12:53] All right. Uh so we'll do year and then
[12:56] year minus one
[12:59] or plus one.
[13:01] Okay. This brings up a thing in computer
[13:03] science dot by one bug. Um
[13:07] um I'm not sure about order of
[13:09] operations too. Minus or the extraction.
[13:11] I'm not sure which one which. I think
[13:13] this is okay, but I might have to put
[13:14] that in parenthesis. Okay. Um but this
[13:17] might be off by one. I don't know. So I
[13:19] was born in 45. So I'll just test it. Or
[13:22] I'm 45 and I was born in 81. So like,
[13:25] hey, you were born in 1981 or 1980.
[13:32] Uh
[13:37] that doesn't track because okay before
[13:39] March I could have been 44
[13:45] does have the same year in it.
[13:54] I do it right.
[14:04] I think I did it right. I'm not going to
[14:06] worry about it. Okay. And then we do a
[14:08] new line character to make that right.
[14:09] Okay. So, if you are 10, you were born
[14:14] in 1916 or 2015. All right. Haha. There
[14:19] we go. That's character input. And this
[14:22] is, you know, we're going to write a lot
[14:23] of programs like this.
[14:25] All right.
[14:28] Oh, and um I would like to point out
[14:30] that I made this an int. So whenever I
[14:32] do this, it automatically parses an int.
[14:34] If that was a double, it would
[14:35] automatically parse it as a double and
[14:38] it takes care of a lot of that. There's
[14:40] some more specifics whenever we want to
[14:43] get it's going to get the next chunk and
[14:46] try to turn it into that thing.
[14:50] So if I want to get your name
[14:57] or string okay so there's a type called
[15:00] string which we haven't talked about and
[15:01] we can get name and we can prompt them
[15:05] for that hey give me your name and we
[15:08] will that in a name and we're going to
[15:12] say
[15:15] uh name
[15:20] Nick, you were born in blah. Okay,
[15:23] that's so I can say, hey, 45,
[15:28] Nick, bam, Nick, you were born in Yeah,
[15:30] that works.
[15:33] Um, but check this out. If I type in
[15:36] this and I type in Nick Stewart, it's
[15:40] only going to get Nick. It's going to
[15:41] get the next chunk. We'll talk about
[15:42] that. We'll circle back. But, you know,
[15:45] we have some issues that we have to deal
[15:47] with eventually, but for the most part,
[15:49] you you give it the type and you read it
[15:51] in like this. Let's keep it simple right
[15:53] now.
[15:56] All right. We got operators. I'm not
[15:57] going to spend too much time about this.
[15:58] If you took programming one, you should
[16:00] know how plus, minus, times, and divide
[16:02] works. You know, order of operations.
[16:04] You should know how the mod operator
[16:05] works. Um, review how you can check for
[16:08] even or oddness. You should know how and
[16:10] and or not works. And um you can use the
[16:13] words and or not lowercase in uh C++ but
[16:18] um it's preferred to use amper amp
[16:19] amperand amperand or um pipe pipe or an
[16:23] exclamation point. Um equal sign works
[16:26] like you're used to. Comparison
[16:28] operators are the same as in Python.
[16:31] This is new brief. uh you can you can
[16:34] you can add or um subtract what's stored
[16:37] in memory um with a plus+ operator.
[16:42] So um
[16:50] if I say year++ it's going to update all
[16:52] the years and make them one bigger and
[16:55] it's kind of a weird thing to do but
[16:57] just as a demo. So I'll be okay. So you
[17:01] can see here I have those years and then
[17:03] I have one more added that you could
[17:05] also do minus minus. It's a pretty handy
[17:07] thing in Python. You had to do plus
[17:09] equal one. Anyways, it's it's it's it's
[17:13] a pretty common thing that most
[17:14] languages have. For some reason, Python
[17:16] just decided not to have the increment
[17:18] decrement operator.
[17:20] All right, we got precedents. You
[17:22] already know this. Parentheses happens
[17:24] first, then unary things. Um so plus
[17:27] signs not the addition sign minus signs
[17:30] not the subtraction not um and logical
[17:34] not and then um increment and decrement
[17:37] which which is new new to us. All right
[17:40] and then we have all the multiplication
[17:42] ones multiplication divide and mod and
[17:45] keep in mind that uh if you have an int
[17:47] divided by an inch you're going to get
[17:48] an int. Um in Python you had a divide
[17:51] and a double divide symbol and depending
[17:54] on whether you want to do float or int
[17:56] division
[17:58] in um
[18:00] in C++ if both sides are ins and you use
[18:02] the division sign like one divided by
[18:04] two you'll get zero. So I should show
[18:06] you that let's just do this right here.
[18:10] divided by two. What is that going to be
[18:15] zero?
[18:20] Oh, I need to run it actually
[18:24] zero. And if I do
[18:28] 99,
[18:30] just to show you that it doesn't always
[18:31] give me zero gives me 49. 49* 2 is 98.
[18:36] So there's a remainder of one. So if I
[18:39] do the complimentary operator, the
[18:42] modulus operator, I'll see that I have
[18:45] one left over.
[18:47] There we go.
[18:49] All right. Got that that that we got
[18:52] relational operators. We got and each of
[18:55] these happen like since this is on this
[18:58] level, they happen at the same time. And
[19:00] so what you do um is you scan across
[19:03] your whole expression and you you
[19:05] evaluate whatever you find times or
[19:07] divide or mod from left to right. And
[19:09] once you process all of those then you
[19:11] go back to the left and you process all
[19:14] the addition and subtraction. And once
[19:16] you process all of that then you go
[19:18] process all the relational operators and
[19:20] then you process all you just do one
[19:22] swipe. You do all the equality
[19:24] operators. Then you do your logical ands
[19:27] then your logical ors and then you do
[19:29] assignment. Anyways, the whole sequence.
[19:35] All right, we can control things with if
[19:37] statements and for loops and we we know
[19:40] these things. Um, let's go look at them.
[19:42] Okay, so if statements work just like
[19:45] Python. We have if, we have else ifs, we
[19:47] have else. The syntax is a little
[19:48] different. I'll leave it to you guys to
[19:50] play around with that. We still have the
[19:52] equal equals versus equal problem that
[19:53] we had in Python. We have parentheses
[19:56] around our conditions. Instead of saying
[19:59] l if we say else if and other and we
[20:02] have curly brackets other than that it
[20:04] pretty much is the same thing.
[20:08] Switch statements I don't use them. I
[20:10] suggest you don't use them. Um I you
[20:12] know it's important that you kind of
[20:14] know how they work in case you ever see
[20:15] stuff and you have to interface with
[20:16] them or it's required of you. I'm not
[20:18] going to require it of you. So basically
[20:20] you just give it something. This will
[20:23] this will evaluate to some value. it'll
[20:24] go match against one of these cases and
[20:26] if it doesn't match against the cases
[20:28] it'll go to the default. I I would
[20:31] challenge you to come up with a
[20:32] situation where a switch statement is
[20:34] the cleanest way to do something. I mean
[20:36] there are some like intermediate
[20:39] programming examples where sometimes
[20:40] they're a little cleaner than an if
[20:42] statement. If statements can get a
[20:44] little bit long, but usually once they
[20:46] start getting too contankerous with if
[20:48] statements, then you can go on to
[20:50] something like an unordered map, um,
[20:52] which we'll talk about eventually. Uh, I
[20:55] think I have some examples in the book
[20:58] of of of other ways you can handle
[21:00] stuff. So, these have these have all
[21:03] sorts of different little bugs that you
[21:05] might have to worry about. You have to
[21:07] worry about breaking and fall through.
[21:09] But anyways,
[21:11] uh I think it's kind of an old
[21:14] antiquated um control um approach.
[21:18] People still like them. Ste people still
[21:20] um suggest them. They have some
[21:22] performance benefits, but like in ways
[21:24] that don't matter to us. So anyway, I'm
[21:27] never going to mention them again. I
[21:29] don't like them. I won't use them. I
[21:31] don't encourage you guys to use them.
[21:33] All right? My bias is clear. But yeah,
[21:35] if you if you like them, use them. I I
[21:38] I'll try to
[21:40] well I'll probably leave a comment to be
[21:42] honest. Okay. Loops you can do for while
[21:46] for um you can do a while, a for a do
[21:49] while
[21:50] um and then you have ways you can break
[21:53] and continue those all of the same
[21:55] things that you did in um Python.
[21:59] Okay, standard for loop looks a little
[22:02] weird. Um so here is you have an
[22:05] initialization you have a condition and
[22:08] you have some way some update. So in
[22:10] this case this will start I at zero
[22:12] it'll print out zero and then after at
[22:14] the end it'll update I to be one bigger
[22:17] and then it'll keep on looping until
[22:19] it's until you get to five. So it'll
[22:22] print 0 1 2 3 4. Once it's five it won't
[22:24] loop anymore.
[22:28] And um this is what I call the standard
[22:30] for loop. And the only thing you need to
[22:31] change here is that number. That'll
[22:33] change how many times you loop. If you
[22:35] want to loop five times, you put a five
[22:36] there. If you want to loop 10 times, you
[22:38] put a 10 there. That's what you pull out
[22:40] if you know how many times you're going
[22:41] to loop. Just throw down a standard for
[22:43] loop, change that number, and then start
[22:45] thinking about what you put on the
[22:46] inside.
[22:48] A while loop, um, I'm doing the same
[22:51] code. Again, you wouldn't normally use a
[22:53] while loop like this. You'd use a for
[22:54] loop. But if I take all the same pieces,
[22:56] the initialization, the update, and the
[22:59] condition, you get the exact same thing.
[23:01] So, we know how while loops work, but we
[23:03] usually use while loops when we don't
[23:05] know how many times we're going to loop.
[23:07] For instance, if you're going to loop a
[23:08] program until the user says they want to
[23:10] exit or something like this, a while
[23:12] loop would be good there. So, even
[23:14] though this doesn't match the example,
[23:16] it's good for unknown iteration counts.
[23:18] All right.
[23:20] Common programming practices. We want to
[23:24] when we have comments, we want to make
[23:26] them meaningful and not just a no duh
[23:30] explain what you can already read from
[23:31] the code. I prefer to have code that's
[23:33] stealth documenting good variable names,
[23:37] good function names, small functions
[23:39] that do one task. Like there's lots of
[23:41] things you can do where comments are
[23:42] almost unnecessary.
[23:45] Um naming, you're going to have good
[23:47] variable names. Don't have bad variable
[23:49] names. If you have if you're counting
[23:51] the number of students, call it numbum
[23:52] students. If you're counting if you're
[23:54] uh if you're storing a color, call it
[23:56] color value or something like this. Make
[23:59] it simple. Make it what it is. Um keep
[24:02] formatting consistent. Uh you will
[24:04] notice that I use curly brackets in the
[24:07] same column most of the time. Um there's
[24:09] going to be some examples um as I'm
[24:11] cleaning up the book where I don't quite
[24:13] always keep that going. But that's
[24:15] that's um that's basically whatever
[24:18] you've been doing in Python with where
[24:19] you indent whenever you're inside of
[24:21] something. All of that's going to apply
[24:23] except we don't have to do that in pi in
[24:25] in C C++. It's whites space independent.
[24:28] So this would run just the same. But for
[24:31] formatting sake, once you have curly
[24:33] brackets, you tab over and once you
[24:34] close curly brackets, you tab back. It
[24:36] makes it very easy to scan and read. Um
[24:39] there's another approach where you have
[24:41] curly brackets on the same line. This
[24:43] makes it hard for me to see that this
[24:44] curly bracket matches up with that one
[24:46] because they're at an angle from each
[24:48] other. I don't like that. I like to see
[24:50] them in the same column and you can draw
[24:51] a line between them. I like that. That's
[24:55] my preference. You guys can use either
[24:56] one. I would say be consistent though.
[24:59] Uh test your code. Um once you become a
[25:02] professional programmer, this will be a
[25:04] big part of your job. You'll actually
[25:05] make formal tests that can be replicated
[25:08] and be run over and over and over again.
[25:10] But um
[25:12] um for for this class, you don't just
[25:15] write a compo a program that runs. Once
[25:17] it runs, that's the first step. You it
[25:20] may or may not be correct. So at this
[25:22] point, you need to try to break your
[25:24] program and make sure that I can't break
[25:28] your program. So you need to if it's
[25:30] asking for an int, try to type in
[25:32] something that's not an int. Um
[25:36] try try to be adversarial with it. um
[25:39] you know um in programming one as long
[25:42] as you as the user followed your
[25:44] directions I would count it as good. Um
[25:47] in programming two you assume the
[25:50] program you assume the user is an idiot
[25:53] and you have to walk them along and get
[25:55] them to wherever you need them to go. So
[25:57] if they can if the user can break your
[25:59] program by just typing in something
[26:00] weird then you need to fix your program.
[26:04] and debugging. Um you can debug
[26:09] um by running and looking error messages
[26:13] um putting print message print things in
[26:15] different places. Um well at some point
[26:17] look at the IDE debugger. I don't want
[26:20] to mess with that right this instant
[26:22] though.
[26:24] All right. Things that you'll mess up in
[26:25] C++
[26:27] or in just general language sometimes
[26:29] but you'll miss a semicolon at the end
[26:31] of statements. Although at if you put
[26:34] them at the end of a for loop, if you
[26:37] put a semicolon there at the end of the
[26:38] for loop, that'll detach the code block
[26:42] or if you put a semicolon here at the
[26:43] end of a while, it'll loop infinitely
[26:45] because that code block's not attached.
[26:48] Or if you uh go to an if and you put a
[26:51] colon here, this code block gets
[26:53] detached and then it'll say like else
[26:54] without an if. So, uh, so you might mess
[26:59] up by forgetting to put a semicolon, but
[27:02] you also might mess up by putting a
[27:03] semicolon someplace where you don't, it
[27:05] doesn't belong. Uh, you can mess up by
[27:07] having a variable that you never give it
[27:09] a value to. So, try to give it a value
[27:11] right away. So, if you're not reading it
[27:12] in from CN character input stream, then
[27:16] um, give it a value whenever you
[27:17] initialize it. Try to avoid having
[27:20] infinite loops. You want to have the
[27:22] loops in. sometimes using equal instead
[27:25] of equal equals whenever you're doing
[27:27] stuff in an if forgetting to include
[27:30] stuff when you need something that's not
[27:32] that's not automatically provided and
[27:34] being off by one happens all the time.
[27:38] All right, debugging tips.
[27:41] You can just read messages.
[27:44] Um you can use the debugger to step
[27:47] through your code and look at what the
[27:48] val state of all the variables and that
[27:50] kind of stuff. You can add print
[27:52] statements.
[27:54] We already talked about debugging
[27:57] and you can just so here's here's the
[27:59] main way to avoid bugs
[28:02] um is just to not write them in the
[28:04] first place. Well, what I mean by that
[28:07] is is we'll start with code that is
[28:09] known to be good and then we'll add a
[28:11] little bit, test it and make sure it's
[28:12] good. Give it some time and then add a
[28:15] little bit more, test it, make sure it's
[28:17] good. If you're building incrementally
[28:21] and not just with one shot, then um
[28:26] then you can you can you can find the
[28:29] bugs as they pop up and you know
[28:31] whatever you just added is probably
[28:32] where the bug came from. Uh maybe do I
[28:36] need to mention AI? AI can produce
[28:38] pretty good code now and it's only going
[28:40] to get better. And this is a class where
[28:42] you need to learn foundational
[28:44] knowledge. So I'm not banning it. you
[28:47] can use it. Um, but there are going to
[28:50] be parts of this class um where you need
[28:54] to know how your code works and need to
[28:56] be able to work with it. Um, and I will
[29:00] test you on that.
[29:02] And if you just
[29:06] put everything from this class into AI,
[29:08] take the results, turn things in, and
[29:11] don't spend any time figuring out what's
[29:14] going on, how build, how to build
[29:15] things, and build this all this muscle
[29:16] memory, you're going to have a severe
[29:19] disadvantage for this class and then
[29:22] also a disadvantage for the future. Like
[29:24] while I think there is a place for
[29:26] future coding where people don't look at
[29:28] it and it's all vibe coded coded on its
[29:32] own without um without the human reading
[29:35] of everything. I think there's a place
[29:37] for that. I think there's also um going
[29:40] to be a huge market for for people that
[29:43] can craft well constructed code that is
[29:48] maybe written by AI but also highly
[29:51] highly designed by humans and and
[29:54] validated by humans and and where humans
[29:58] are keeping it on rails and not just
[30:00] letting it be anything willy-nilly.
[30:04] Um that I might be wrong. Um but you
[30:08] know I think there's always a market for
[30:11] people that um are are interested to
[30:14] learn learn things are are you know
[30:16] respect the craft
[30:18] but could be could be way wrong. So um
[30:22] but anyways in this class this class is
[30:24] to give you fundamental skills. That's
[30:26] the goal. I need to validate that you
[30:29] have fundamental programming skills and
[30:31] so you need to work to get those
[30:33] fundamental programming skills. Well, I
[30:36] know that that AI can do all the things
[30:38] in this class and you're free to use it
[30:41] as a tutor, as a coding partner. You can
[30:44] use it for all of those things. Uh you
[30:46] just need to make sure that you're not
[30:48] undermining your own learning and I will
[30:51] test you to see if you are getting the
[30:53] fundamental skills because that is my
[30:55] job to make sure you have fundamental
[30:57] skills. So, there will be some tests um
[31:00] where you have to to do stuff without
[31:02] AI. All right,
[31:04] let's see what else we got. Dos and
[31:08] don'ts. Uh, uh, always initialize
[31:10] variables when declaring them. Give them
[31:12] values. Use variable meaningful variable
[31:15] names. Include necessary header files.
[31:16] We haven't talked about that. Use good
[31:18] formatting. Test programs. Use
[31:21] parenthesi. I we didn't talk about this
[31:23] one, but use parentheses. If the order
[31:24] of operations gets confusing to you,
[31:26] just use parenthesis. You can always
[31:28] enforce whatever order that you want.
[31:31] Um, don't use single variable names
[31:33] except whenever you're in loops or stuff
[31:35] like that. Don't forget semicolons
[31:37] except don't don't put them at the after
[31:39] the if, right? That would be bad. Don't
[31:42] use equal for comparison. Don't create
[31:44] infinite loops.
[31:46] Uh, and I don't I don't think you should
[31:49] worry about this, but don't uh don't
[31:50] assume specific types across platforms.
[31:53] You know, for the most part, you guys
[31:54] are going to be programming for a PC.
[31:56] The the ins are going to be four bytes.
[31:58] The doubles are going to be eight bytes.
[32:00] It's going to be consistent.
[32:04] All right.
[32:08] Do I need to read this? Let's see. C++
[32:11] is a compiled language require uh
[32:13] requiring compilation before execution
[32:14] as opposed to Python that's interpreted.
[32:17] It is way faster. So much faster.
[32:20] Hundreds of times faster. Proper program
[32:23] structure with main. Um, it's essential.
[32:27] You have to have a main in every single
[32:28] program. Otherwise, you the program
[32:30] doesn't know where to start. You need to
[32:32] understand data types. In Python, you
[32:34] could just, you know, have a variable
[32:36] and put anything into it willy-nilly and
[32:38] change what's in it. But in in C++, you
[32:41] have to say, hey, this is going to store
[32:42] this and it and it has to be of this
[32:45] type and it can never change. Um,
[32:48] operators still have precedents. Um, so
[32:50] I I feel like you guys probably know
[32:51] that control flow structures enable
[32:54] complex programs. You should already
[32:55] know that and good programming practices
[32:59] prevent common errors. So yeah, using
[33:01] good formatting, good variable names,
[33:04] incremental programming, all of this
[33:05] stuff can lead to like, you know, way
[33:08] less struggle.
[33:10] All right. So what uh what what could
[33:14] you do to go forward? Well, these are
[33:16] all things that we're going to talk
[33:16] about in the future, but usually this
[33:18] slide is some weird wacky topics that
[33:20] you can just dig in and go farther. But
[33:22] these are all things we will do. So,
[33:24] we're going to talk about advanced data
[33:25] types like arrays and vectors and
[33:27] strings. Um, we're going to talk about
[33:30] um functions. We haven't done any
[33:32] function stuff or object programming.
[33:34] We'll do that. Um there's a bunch of
[33:37] fancy modern C++ features like lambdas
[33:40] and rangebased for loops there. Um the
[33:43] standard library has a bunch of cool
[33:44] things embedded in it. Containers,
[33:46] algorithms, iterators.
[33:48] And um one thing that C makes C++
[33:51] different definitely from um Python is
[33:54] that it's lowlevel and has memory
[33:57] management where you directly do the
[33:59] memory management. Python does it all
[34:01] for you. Um, but then you can't use it
[34:04] to make device drivers and stuff like
[34:06] this because you don't have in you don't
[34:07] have you don't have you don't have um
[34:12] what do you call it? Um you don't have
[34:15] like really
[34:18] what's the word? You don't you don't you
[34:21] you can't do anything specifically in
[34:22] memory. you don't have control over it.
[34:25] Where in C++ you can actually reach into
[34:27] memory and change this bit to that and
[34:30] you have you have complete control.
[34:32] Scary amount of control but that control
[34:35] can also shoot you in the foot. So
[34:38] there you go.
