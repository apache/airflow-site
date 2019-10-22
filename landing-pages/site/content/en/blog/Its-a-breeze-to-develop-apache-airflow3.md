---
title: "It's a breeze to develop Apache Airflow"
linkTitle: "It's a breeze to develop Apache Airflow"
author: "Jarek Potiuk"
description: "Working on an Open Source project such as Apache Airflow is very demanding but also equally rewarding when you realize how many businesses use it every day."
tags: ["Python"]
date: 2019-09-24
---

##### My journey to developer productivity
It started at the beginning of my career with my older and more experienced colleague—one of the first “real” software engineers I had interacted with by then. I learned a lot from him. I specifically remember him saying: “When I develop code, I spend the first half of my time on developing tools to make my work 10x faster—that’s the key reason why I always deliver on time.” His words stuck with me. I’ve been a part of many successful projects in my career but they pretty much always looked like this: when I first joined a project I’d look around, trying to learn the ropes and identify bottlenecks, such as the lack of tools or what part of the development process could slow me down.

As an All-Stack-Engineer, I believe the best use of my time is to put my efforts not only to the code that I deliver but mainly to develop all the tools, DevOps setup, continuous integration, automated code analysis and everything essential for the developers. The best-case scenario is when your developers can use them independently and you don’t need to worry about them.

{{< highlight js >}}
// Synchronize user data and set up
var currentUser = new Talk.User({
    id: 79302,                      // user id
    name: "George Looney",          // full name
    email: "george@looney.net"      // for offline email fallback
});
var session = new Talk.Session({
    appId: "9352938974",            // your TalkJS account id
    me: currentUser                 // make George the active user
});
{{< /highlight >}}

##### What do I mean by productivity
How do you define productivity though? And how can you measure it? I have a possibly surprising answer—it’s not about a number of lines of code you’ve written or features you’ve delivered. Productivity is something rather different. It’s all about focusing on the present and the future rather than the past. Productivity is more of a bet that in the future your team will be able to deliver more at the same time. It has way more to do with your perceived speed and enjoying work as a developer than the outcome of work you’ve already done. It is about building the potential for future gains while focusing on delivering the project.

I could think of a number of projects where I followed that philosophy of work and where it boosted the productivity of my team. Today, however, I’d like to focus on Apache Airflow.

##### The Apache Airflow project’s setup
Initially, we started contributing to this fantastic open-source project with a team of three which then grew to five. When we kicked it off a year ago, I realized pretty soon where the biggest bottlenecks and areas for improvement in terms of productivity were. Even with the help of our client, who provided us with a “homegrown” development environment it took us literally days to set it up and learn some basics.

Apache Airflow is a thoroughly tested project—it has almost 4,000 tests with around 80% coverage and varying complexity (from simple unit tests to end-to-end system tests). Airflow follows a modern software project philosophy: every single Pull Request can only be merged if all the tests pass. But that creates another problem—having to run all the tests for all the backends (there are 3 of them) and different python versions. At the time of starting the project we still supported 2.7, 3.5 and 3.6—so you had to wait sometimes for several hours to have the results of the CI build, depending on the delays and queues. At times, you have no control over the CI system you use. For example, recently we experienced hours of delays before we could even see the build starting.

This is hardly acceptable to any developer. Usually you can work on several issues in parallel. Such waiting is not the worst thing that can happen, but there are always costs of context-switching, distractions, getting out of the flow and the good old “I already forgot what I was doing” phase by the time the build is completed. It’s even worse when you want to make a small Pull Request. For example, when you find a bug and have just one line of fix for it. You submit the Pull Request and… half a day later you see that your single line of code change is badly formatted.
