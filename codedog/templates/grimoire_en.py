# flake8: noqa

"""Grimoire of CodeDog. English version."""

# -- PR Review Prompt Template ---------------------------------------------------

# this template is used for format diff file summary list seperate important and housekeeping changes.
PR_FILES_SUMMARY_HEADER = """
**Main changes**
{important_changes}
**Secondary changes**
{unimportant_changes}
"""

PR_FILE_SUMMARY_HEADER = "{path}: {summary}"


# this template is used for review single file change.
PR_CHANGE_REVIEW_SUMMARY = "summary of diff"
PR_CHANGE_REVIEW_MAIN_CHANGE = """this diff contains the major part of logical changes in this change list"""

PR_CHANGE_REVIEW_TEMPLATE = """
Act as a code reviewer, I will be your assistant, provide you a file diff in a change list,
please review the code change according to the following requirements:

1. Determine whether the file is a code file containing major logic changes. Generally speaking,
such files often have some function logic changes

2. Briefly summarize the content of the diff change in Chinese, no more than 100 words,
do not include the results of the first step, just summarize the content of the change.

{format_instructions}

Please act as a code reviewer, review the file {name} change. I want you to give:
1. Determine whether the file contains major logic changes. Generally speaking,
2. A brief summary of the diff change, no more than 100 words. Do not include the results of the first step

review the code according to the instructions:

{format_instructions}

here is the diff content:
```
{text}
```"""

PR_CHANGE_REVIEW_FALLBACK_TEMPLATE = """
Please act as a code reviewer, review the file {name} change. I want you to give:

give a brief summary of the diff change, no more than 100 words.

here is the diff content:
```
{text}
```"""

# this template is for starting sequentially summarize PR content.
PR_SUMMARIZE_TEMPLATE = """
Summarize a git pull request by the given information:

pull request information (for better understand the context, not part of the pull request):
```
{pull_request_info}
```
related issue information (for better understand the context, not part of the pull request):
```
{issue_info}
```

changes summary:
```
{summary}
```

Please note that I want you to summarize the entire pull request, not specific files.
The summary should be no more than 200 words:"""


PR_SIMPLE_FEEDBACK_TEMPLATE = """
Act as a code reviewer, I will be your assistant, provide you a file diff from a change list,
please review the code change according to the following requirements:

1. Don't give subjective comments on the code quality, such as "this code is bad", "this code is good", etc.
2. Don't give general suggestions that are not specific to the code, such as "this code needs to be refactored", "this code needs to be optimized", etc.

If you can't judge whether the code is good or bad, please reply "ok" and don't reply any other content except "ok".

Here's the code:
{text}
"""
