---
title: "Roadmap"
linkTitle: "Roadmap"
showSideNav: false
---

TODO: Roadmap page is temporarily hidden. When the content is ready, re-add the page by putting the following code
in the frontmatter:

    ---
    title: "Roadmap"
    linkTitle: "Roadmap"
    showSideNav: false
    menu:
      main:
        weight: 15
    ---

## Primary Heading A

One thing to wrap your head around (it may not be very intuitive for everyone at first) is that this Airflow Python
script is really just a configuration file specifying the DAG’s structure as code. The actual tasks defined here will
run in a different context from the context of this script. Different tasks run on different workers at different
points in time, which means that this script cannot be used to cross communicate between tasks. Note that for
this purpose we have a more advanced feature called XCom.

People sometimes think of the DAG definition file as a place where they can do some actual data processing -
that is not the case at all! The script’s purpose is to define a DAG object. It needs to evaluate quickly (seconds,
not minutes) since the scheduler will execute it periodically to reflect the changes if any.

People sometimes think of the DAG definition file as a place where they can do some actual data processing - that is not the case at all! The script’s purpose is to define a DAG object. It needs to evaluate quickly (seconds, not minutes) since the scheduler will execute it periodically to reflect the changes if any.

## Primary Heading B

One thing to wrap your head around (it may not be very intuitive for everyone at first) is that this Airflow Python
script is really just a configuration file specifying the DAG’s structure as code. The actual tasks defined here will
run in a different context from the context of this script. Different tasks run on different workers at different
points in time, which means that this script cannot be used to cross communicate between tasks. Note that for
this purpose we have a more advanced feature called XCom.

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

## Primary Heading C

One thing to wrap your head around (it may not be very intuitive for everyone at first) is that this Airflow Python
script is really just a configuration file specifying the DAG’s structure as code. The actual tasks defined here will
run in a different context from the context of this script. Different tasks run on different workers at different
points in time, which means that this script cannot be used to cross communicate between tasks. Note that for
this purpose we have a more advanced feature called XCom.

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

## Primary Heading D

One thing to wrap your head around (it may not be very intuitive for everyone at first) is that this Airflow Python
script is really just a configuration file specifying the DAG’s structure as code. The actual tasks defined here will
run in a different context from the context of this script. Different tasks run on different workers at different
points in time, which means that this script cannot be used to cross communicate between tasks. Note that for
this purpose we have a more advanced feature called XCom.

People sometimes think of the DAG definition file as a place where they can do some actual data processing -
that is not the case at all! The script’s purpose is to define a DAG object. It needs to evaluate quickly (seconds,
not minutes) since the scheduler will execute it periodically to reflect the changes if any.

People sometimes think of the DAG definition file as a place where they can do some actual data processing - that is not the case at all! The script’s purpose is to define a DAG object. It needs to evaluate quickly (seconds, not minutes) since the scheduler will execute it periodically to reflect the changes if any.
