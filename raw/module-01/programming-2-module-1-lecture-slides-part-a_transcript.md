# Transcript: Programming 2: Module 1 (Lecture Slides Part A)

[00:02] All right, let's do module one,
[00:05] fundamentals of C++.
[00:08] Um the reading is probably important
[00:11] here if you are missing some of this,
[00:14] but um this will kind of give you an
[00:16] overview.
[00:17] uh in the future modules um the uh these
[00:21] slides will will probably be a better
[00:23] summary, but there's just so much um to
[00:26] go over for this first bit that I really
[00:29] encourage you guys to skim through all
[00:30] the reading for sure. All right, let's
[00:34] do this.
[00:36] All right, learning objectives. You guys
[00:39] can read. We're going to learn about all
[00:42] the stuff.
[00:45] Okay. So, um you already know some of
[00:48] this stuff. We got source code. That's
[00:49] what you can read. We uh there's a
[00:51] compilation pro process. We write write
[00:53] code. We compile it. We test debug and
[00:57] then repeat. Um that's not just the
[01:00] compile that's not the compile process,
[01:02] that's the development process. Um so
[01:05] you need to be able to like make small
[01:07] little changes, make sure it works,
[01:08] iterate on it. Um
[01:12] same thing that you've done in
[01:13] programming one. All right. Um, in a um,
[01:18] in C++ the main function is the entry
[01:22] point. Whenever you're in Python, you
[01:24] can just hit run and it runs the code.
[01:27] In C++, you have to have a special
[01:30] function called the main that goes and
[01:32] runs. Let me pull that up.
[01:35] Code bin. Uh, code bin is a tool I
[01:39] provide. Um, if you Google it, you won't
[01:42] find anything. I have a link in the uh
[01:44] CL in on the classroom site
[01:48] and uh you can just write some simple
[01:50] code. You can run it right in the
[01:52] browser. You guys can do this on your
[01:55] own personal computer if you have a
[01:57] setup. But um anyways, easy way to test
[02:00] code and on top of that you can hit the
[02:03] share button. It'll give you a little
[02:05] link to this particular bit of code. It
[02:08] takes a second. It'll automatically be
[02:09] in your clipboard. you can share that
[02:11] with me if you ever have questions. Uh
[02:14] you can you can share on the discord,
[02:15] email me, whatever you need. But uh here
[02:18] you can see a very basic hello world
[02:21] program. You know, that's what you
[02:23] always do when you first start writing
[02:25] code. Um you have to have this function
[02:27] called int main. Um and whenever you
[02:30] compile stuff, when you go to run it, it
[02:33] looks for a main function to go start
[02:35] here and then it starts in inside of
[02:37] here.
[02:39] you don't have something called main
[02:40] like I make this a capital M
[02:45] it won't work. We'll see what the error
[02:47] message is. It says hey we didn't find a
[02:50] main
[02:52] and so you have you have to have this
[02:55] entry point. All right. There we go.
[02:58] Entry point. I keep on hitting control
[03:01] S. Okay.
[03:05] All right. Um Okay. So then um I guess
[03:08] we can talk about the rest of this. Uh
[03:10] there's an include up here. We have to
[03:12] include that so we can get the out
[03:14] character output stream and the
[03:15] character input stream and stuff like
[03:17] this. Uh just like in Python you have to
[03:19] import here we have to include.
[03:21] Basically what this does um is it uses
[03:24] what's called the pre-processor and it
[03:26] goes and grabs code from somewhere else
[03:28] and like plops it here. So basically
[03:30] this file has more code in it than it
[03:33] originally had. So all the code comes
[03:34] together and then you compile that. Um
[03:39] so that's what's happening here.
[03:43] Um compilation command. Okay. So you're
[03:47] not going to have to do this maybe at
[03:49] all, but um um from the terminal, if you
[03:53] have a computer that has the GNU C
[03:56] compiler
[03:58] installed on it, you can compile a
[04:00] program using some code like this.
[04:03] So, um you can say g++ and then um and
[04:09] then you can give it a target name. Um
[04:12] if you're on Windows that would be
[04:14] likeexe. So you the pro Windows knows
[04:16] how to run it but on on like pro on on
[04:19] things like Linux and and Mac you can
[04:22] run programs that don't have a.exe
[04:24] extension and this is the source files
[04:27] that you're going to compile into that.
[04:31] any these things can get much more
[04:33] complicated. There going to be much more
[04:35] flags yada yada. Um
[04:38] it's important to know that there is
[04:41] everything's happening in everything can
[04:44] be done at the terminal. We're just
[04:46] providing extra tools to make your life
[04:49] easier with things like IDE um
[04:52] integrated development environments
[04:53] which you guys probably know.
[04:56] Anyways, for the most part, we'll have
[04:59] run buttons and it'll it'll do things in
[05:02] the background. Compile and then run.
[05:04] All right, we got a basic program. Um,
[05:07] every statement needs a semicolon. So,
[05:10] we got semicolon here, semicolon here.
[05:12] We do not have a semicolon here because
[05:15] this fun, this line connects to this
[05:18] code block.
[05:20] That's equivalent to like in um
[05:24] um if you did this in Python, you would
[05:26] do that and then you tab everything over
[05:28] and that's all inside of that. So um
[05:33] that is that.
[05:36] All right. Uh we got to have a main. You
[05:38] got to return zero. Well, you don't have
[05:40] to have a return zero, but you should.
[05:42] This function expects an int to be
[05:44] returned. So here I return a zero. Why
[05:47] return zero? Why does this have to have
[05:49] an int? They just decided and but uh the
[05:53] cool thing is is whenever you if you
[05:55] have a pro not this program but another
[05:57] program run this program you can get
[06:00] information back on how it exited. So uh
[06:04] a return zero may ba basically is a
[06:06] thumbs up like hey everything finished
[06:07] fine but if I return something like one
[06:09] or something like this it'll be um or
[06:12] any any other number zero basically code
[06:16] to to whatever program called this that
[06:19] something went wrong and you can make
[06:20] those numbers mean something. So it's
[06:22] basically like a return value but for a
[06:25] whole program. And so you can
[06:29] specifically in the Linux world you can
[06:31] chain different programs together and
[06:33] treat them kind of like functions.
[06:36] So um but yeah for the most part you
[06:40] just return zero. Don't worry about it.
[06:43] All right
[06:46] got that. All right we got variables and
[06:48] data types. So in in Python
[06:51] you could just say hey we have x is
[06:54] equal to 5 and we're done. No semicolon
[06:57] but in here we need a semicolon and we
[06:59] have to tell it what kind of thing we're
[07:01] storing. So we have to say int. So you
[07:05] can define it and then later you can
[07:07] assign to it. Um, one thing that's going
[07:10] to look a little weird is whenever you
[07:13] um whenever you can say int x= 5 and
[07:17] that's common to like most other
[07:19] languages, but for some reason in C C++
[07:22] the most the most accepted way to to do
[07:26] initialization is with curly brackets
[07:28] here.
[07:30] And that that'll that'll I'm going to
[07:32] try to do it this way. Um and and
[07:35] there's going some other syntax in the
[07:37] future that if you get in the habit of
[07:38] doing this, it makes some other stuff in
[07:41] the future a little bit easier. But um
[07:43] you could do this or you can say equals
[07:46] 5. They're basically equivalent. Uh the
[07:48] compiler basically optimizes it away and
[07:51] makes them the same. Technically there's
[07:52] there's they mean different things. Uh
[07:55] this is what's called copy
[07:56] initialization, I want to say. So it
[07:59] takes whatever values on the right and
[08:01] copies it on the thing on the left. Um,
[08:03] but this is I think called direct memory
[08:06] initialization. So it just takes this
[08:08] value and plops it straight into memory
[08:10] without doing a copy. Uh, I'm I honestly
[08:17] I I
[08:19] like there is a difference and sometimes
[08:20] it matters but it doesn't matter. So um
[08:26] anyways so you can you can tell X that
[08:29] it's an int once. You can't later tell
[08:31] it's a double. You can't You can't tell
[08:33] it it's an int again. You can only tell
[08:35] it once. But you can change it as many
[08:37] times as you want. And after the first
[08:39] time, you use equal sign like you're
[08:41] used to. And then you can then um you
[08:44] can print out variables just same things
[08:47] we've been doing in um programming one.
[08:50] But you know the syntax is a little
[08:52] different. I guess I should explain what
[08:55] standard out does. I don't know if I
[08:58] have a slide for that. that um okay so
[09:01] we have io stream that allows us have
[09:03] access to this variable standard see out
[09:05] colon see out so what is a colon this
[09:09] lets you get something in a namespace so
[09:11] there's the standard namespace which
[09:13] most of the standard libraries use so so
[09:17] there's this this you know area we can
[09:19] bas basically we can we can put things
[09:22] in this box over here called standard
[09:24] and so there's a variable inside of that
[09:26] called see out So um there is a thing
[09:30] you can do uh you could say using name
[09:34] space
[09:38] std
[09:39] and then you can get rid of the this the
[09:42] standard part of it
[09:45] but that is um something that I will
[09:48] count off on. What's happening here is
[09:50] you're taking everything in that box and
[09:52] you're just obliterating the boundary
[09:54] and then bringing all of those variables
[09:56] into your namespace. And so if there's
[09:59] any variables in that namespace that
[10:01] interffect interact with variables you
[10:04] already have, you're going to have some
[10:05] issues. It's called polluting the
[10:08] namespace. This is this is very
[10:10] discouraged nowadays. So don't do that.
[10:14] And for the few times you have to print,
[10:16] you have to say standard colon. You have
[10:18] to type a little bit extra, but it's
[10:20] really not that big of a deal. All
[10:23] right, so here we have the character
[10:26] output stream. That's what we have here.
[10:28] We have the insertion operator. You can
[10:30] think of it as a conveyor belt. It will
[10:32] take X and conveyor it into the
[10:34] character output stream. And then it'll
[10:37] go onto the screen. And once this
[10:41] operator applies itself, takes the thing
[10:44] on the left and the right does work. in
[10:46] this case takes X and puts it in the
[10:48] character stream on the on the the the
[10:51] left is going to give you back the
[10:54] character output stream. So after that
[10:57] processes it, it will it will now X will
[11:00] now be on the screen and it'll give you
[11:02] back the character output stream which
[11:04] will let you feed, you know, conveyor
[11:06] another thing into the character output
[11:08] stream. So you can just basically line
[11:11] up a whole bunch of things over to the
[11:13] right and just and print them one after
[11:14] the other.
[11:16] a little different than you probably
[11:18] ever seen before, but that's all you
[11:19] have to do. Car see out, you know,
[11:21] insertion operator thing you want to
[11:23] print. Insertion operator thing you want
[11:24] to print, so on so forth. Now, standard
[11:28] inline, what is that?
[11:30] That is obviously the end uh that that's
[11:33] a new line character. You can also do um
[11:37] this
[11:39] back slash in that's an escape character
[11:40] for a new line. Both of those are
[11:42] basically interchangeable. they
[11:44] technically are difference. Um this one
[11:47] um this one will flush the uh buffer and
[11:50] will make sure things show up on the
[11:52] screen. The other one won't. But in
[11:54] practice there is no difference. Um most
[11:57] of the time um if you have if you if you
[12:00] later like the reason that you might
[12:02] want something flushed onto the the
[12:04] screen
[12:06] um let's say you do this and then you
[12:08] ask the user for something you do
[12:10] standard CN
[12:12] uh CN and we try to feed whatever they
[12:14] type in into some other variable. We'll
[12:17] we'll look at that in a second. But if
[12:19] we do that, um, the act of waiting with
[12:21] the keyboard for somebody to type
[12:23] something usually will flush the buffer
[12:25] also.
[12:26] But potentially you could get yourself
[12:28] in a situation where you might need to
[12:30] flush the buffer,
[12:33] but I wouldn't worry about it.
[12:37] All right, so we got we can declare
[12:39] variables. We can initialize variables
[12:41] one of these two ways. We can assign
[12:43] variables. We talked about this. And
[12:45] then best practice always initialize
[12:47] variables when declaring. That's a
[12:48] that's an important note you can make in
[12:51] a variable int y then you can use that
[12:54] variable and you can run
[12:58] and it will give me zero. This one gave
[13:00] me zero but it could have been anything.
[13:03] I didn't give it a value so it could be
[13:05] any value. Um, this compiler with these
[13:08] settings happened to put zero there. But
[13:11] other compilers with different settings
[13:12] could just leave whatever memory is
[13:14] there there and it could just be random
[13:16] bits from whatever whoever used that bit
[13:19] of memory last.
[13:21] You get what's called undefined
[13:22] behavior. This is really bad. Do not
[13:25] count on that being zero.
[13:28] That's all I need to say about that.
[13:35] Sorry about that. All right, we got
[13:37] bool. Here's all the different types.
[13:40] Um, some of the fundamental types.
[13:42] There's more, but um, we got bool, char,
[13:44] int, float, and double. Uh, bool. Um, we
[13:48] won't use right away, but we will
[13:50] actually we will use right away.
[13:51] Anyways, that's your true and false
[13:53] values. Um,
[13:56] and then we got chars um, which are
[13:59] single characters. We can put single
[14:01] characters together in a string. We'll
[14:02] talk about that in a second. You have
[14:05] int. int can store plus or minus 2
[14:08] billion which is big. Um not shown here
[14:14] which should be shown here is a long
[14:15] which is uh an eight bite version of an
[14:19] int and it can store um plus or minus 2
[14:24] to the 63rd which is
[14:28] you know like a billion billion a
[14:30] trillion billion like it's very big
[14:33] numbers. So if you're counting if you're
[14:34] doing like polling on the global scale
[14:37] like um its won't cut it. So sometimes
[14:40] you'll run out of space and you'll get
[14:42] crazy overflow issues. Here, let let me
[14:44] show you an overflow issue real quick.
[14:47] Um, all right. So, let's do a billion.
