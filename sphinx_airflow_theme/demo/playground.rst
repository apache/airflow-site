 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Playground
==========

.. contents:: Content
  :local:
  :depth: 1

Inline markup
"""""""""""""

*text* - emphasis (italics),
**text** - emphasis (boldface), and
``text`` - code samples.


List and quotes blocks
""""""""""""""""""""""

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

Subsection
''''''''''

Subsubsection
-------------

Definitions list
""""""""""""""""

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

Parameter list
""""""""""""""

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer

Option list
"""""""""""

-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.

Literal blocks
""""""""""""""

This is a typical paragraph.  An indented literal block follows.

::

    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print a
    print "it's..."
    # a literal block continues until the indentation ends

This text has returned to the indentation of the first paragraph,
is outside of the literal block, and is therefore treated as an
ordinary paragraph.


Quoted literal blocks
"""""""""""""""""""""

John Doe wrote::

>> Great idea!
>
> Why didn't I think of that?

You just did!  ;-)


Doc test blocks
"""""""""""""""

This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

The following is a literal block::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!


Grid tables
"""""""""""

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+


Footnotes
"""""""""

[#]_ is a reference to footnote 1, and [#]_ is a reference to
footnote 2.

.. [#] This is footnote 1.
.. [#] This is footnote 2.
.. [#] This is footnote 3.

[#]_ is a reference to footnote 3.


[2]_ will be "2" (manually numbered),
[#]_ will be "3" (anonymous auto-numbered), and
[#label]_ will be "1" (labeled auto-numbered).

.. [2] This footnote is labeled manually, so its number is fixed.

.. [#label] This autonumber-labeled footnote will be labeled "1".
   It is the first auto-numbered footnote and no other footnote
   with label "1" exists.  The order of the footnotes is used to
   determine numbering, not the order of the footnote references.

.. [#] This footnote will be labeled "3".  It is the second
   auto-numbered footnote, but footnote label "2" is already used.


Here is a citation reference: [CIT2002]_.

.. [CIT2002] This is the citation.  It's just like a footnote,
   except the label is textual.


Para.

----------

Para.


Admonitions
"""""""""""

.. attention::
   Beware killer rabbits!

.. caution::
   Beware killer rabbits!

.. danger::
   Beware killer rabbits!

.. error::
   Beware killer rabbits!

.. hint::
   Beware killer rabbits!

.. important::
   Beware killer rabbits!

.. note::
   Beware killer rabbits!

.. tip::
   Beware killer rabbits!

.. warning::
   Beware killer rabbits!


.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.


.. versionadded:: 2.5
   The *spam* parameter.

.. versionchanged:: 2.5
   The *spam* parameter.

.. deprecated:: 2.5
   The *spam* parameter.


.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`

.. rubric:: AAAAAA


.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

Figure
""""""

.. figure:: awesome-cat.jpg
   :scale: 10 %
   :alt: Photo by Jae Park on Unsplash

   Awesome cat because everyone loves cats.


Topic
"""""

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

Sidebar
"""""""

.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.


Code
""""

.. code:: python

  def my_function():
      "just a test"
      print 8/2


rubric
""""""

.. rubric:: I like kitty

Epigraph
""""""""

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai


compound
""""""""


.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.


Table of Contents
"""""""""""""""""

.. contents:: Table of Contents


Awesome
"""""""

.. header:: This space for rent.


Replacement Text
""""""""""""""""

.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.


I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around
.. _Python: http://www.python.org/


Unicode Character Codes
"""""""""""""""""""""""

Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign
.. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:


Date
""""

.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.


Roles
"""""
:envvar:`envvar`

... is installed in :file:`/usr/lib/python2.{x}/site-packages` ...

The function :py:func:`datetime.datetime.today()` does a similar thing.

The function :py:class:`datetime.datetime` does a similar thing.

The function :py:class:`datetime.INVALID` does a similar thing.


Class description
"""""""""""""""""

https://airflow.readthedocs.io/en/latest/_api/airflow/contrib/hooks/gcp_api_base_hook/index.html

.. py:class:: GoogleCloudBaseHookDDD(gcp_conn_id:str='google_cloud_default', delegate_to:str=None)

   Bases: :class:`airflow.hooks.base_hook.BaseHook`

   A base hook for Google cloud-related hooks. Google cloud has a shared REST
   API client that is built in the same way no matter which service you use.
   This class helps construct and authorize the credentials needed to then
   call googleapiclient.discovery.build() to actually discover and build a client
   for a Google cloud service.

   The class also contains some miscellaneous helper functions.

   All hook derived from this base hook use the 'Google Cloud Platform' connection
   type. Three ways of authentication are supported:

   Default credentials: Only the 'Project Id' is required. You'll need to
   have set up default credentials, such as by the
   ``GOOGLE_APPLICATION_DEFAULT`` environment variable or from the metadata
   server on Google Compute Engine.

   JSON key file: Specify 'Project Id', 'Keyfile Path' and 'Scope'.

   Legacy P12 key files are not supported.

   JSON data provided in the UI: Specify 'Keyfile JSON'.

   :param gcp_conn_id: The connection ID to use when fetching connection info.
   :type gcp_conn_id: str
   :param delegate_to: The account to impersonate, if any.
       For this to work, the service account making the request must have
       domain-wide delegation enabled.
   :type delegate_to: str

   .. py:function:: send_message(sender, recipient, message_body, [priority=1])

       Send a message to a recipient

       :param str sender: The person sending the message
       :param str recipient: The recipient of the message
       :param str message_body: The body of the message
       :param priority: The priority of the message, can be a number 1-5
       :type priority: integer or None
       :return: the message id
       :rtype: int
       :raises ValueError: if the message_body exceeds 160 characters
       :raises TypeError: if the message_body is not a basestring

   .. py:staticmethod:: send_message

       Send a message to a recipient

   .. py:staticmethod:: send_message

       Send a message to a recipient

   .. py:classmethod:: send_message

       Send a message to a recipient

   .. py:decorator:: send_message

       Send a message to a recipient

   .. py:decoratormethod:: send_message

       Send a message to a recipient


   .. attribute:: project_id


      Returns project id.

      :return: id of the project
      :rtype: str


   .. attribute:: num_retries


      Returns num_retries from Connection.

      :return: the number of times each API request should be retried
      :rtype: int


   .. attribute:: client_info


      Return client information used to generate a user-agent for API calls.

      It allows for better errors tracking.

      This object is only used by the google-cloud-* libraries that are built specifically for
      the Google Cloud Platform. It is not supported by The Google APIs Python Client that use Discovery
      based APIs.


   .. attribute:: scopes


      Return OAuth 2.0 scopes.

      :return: Returns the scope defined in the connection configuration, or the default scope
      :rtype: Sequence[str]



   .. method:: _get_credentials_and_project_id(self)

      Returns the Credentials object for Google API and the associated project_id




   .. method:: _get_credentials(self)

      Returns the Credentials object for Google API




   .. method:: _get_access_token(self)

      Returns a valid access token from Google API Credentials




   .. method:: _authorize(self)

      Returns an authorized HTTP object to be used to build a Google cloud
      service hook connection.




   .. method:: _get_field(self, f:str, default:Any=None)

      Fetches a field from extras, and returns it. This is some Airflow
      magic. The google_cloud_platform hook type adds custom UI elements
      to the hook page, which allow admins to specify service_account,
      key_path, etc. They get formatted as shown below.




   .. staticmethod:: catch_http_exception(func:Callable[..., RT])

      Function decorator that intercepts HTTP Errors and raises AirflowException
      with more informative message.




   .. staticmethod:: fallback_to_default_project_id(func:Callable[..., RT])

      Decorator that provides fallback for Google Cloud Platform project id. If
      the project is None it will be replaced with the project_id from the
      service account the Hook is authenticated with. Project id can be specified
      either via project_id kwarg or via first parameter in positional args.

      :param func: function to wrap
      :return: result of the function call




   .. staticmethod:: provide_gcp_credential_file(func:Callable[..., RT])

      Function decorator that provides a ``GOOGLE_APPLICATION_CREDENTIALS``
      environment variable, pointing to file path of a JSON file of service
      account key.
