# postwriter - a python tool to turn some data about blog posts into html that is pasted into index.html

# NOTE the pasting is manual, I do not have the time or skill to to insertion of blocks of HTML into webpages

import colorama as cl # used for pretty text formatting

import datetime # used to the UTC timestamp for post filenames
import calendar # ^

import markdown # markdown articles -> html

cl.init()

# title prompt

p_title = input(cl.Fore.YELLOW + cl.Style.BRIGHT + "% " + cl.Fore.GREEN + cl.Style.NORMAL + "What will the " + cl.Fore.CYAN + cl.Style.BRIGHT + "post " + cl.Fore.GREEN + cl.Style.NORMAL + "be titled?: " + cl.Fore.YELLOW)
print(cl.Style.RESET_ALL)

# data prompt

p_date = input(cl.Fore.YELLOW + cl.Style.BRIGHT + "% " + cl.Fore.GREEN + cl.Style.NORMAL + "What's the " + cl.Fore.CYAN + cl.Style.BRIGHT + "date " + cl.Fore.GREEN + cl.Style.NORMAL + "?: " + cl.Fore.YELLOW)
print(cl.Style.RESET_ALL)

# content prompt

p_content_fname = input(cl.Fore.YELLOW + cl.Style.BRIGHT + "% " + cl.Fore.GREEN + cl.Style.NORMAL + "Where is the " + cl.Fore.CYAN + cl.Style.BRIGHT + "content " + cl.Fore.GREEN + cl.Style.NORMAL + "being stored (" + cl.Style.DIM + "post.md" + cl.Style.NORMAL + ")?: " + cl.Fore.YELLOW)
print(cl.Style.RESET_ALL)

if p_content_fname == "": p_content_fname = "post.md"

# load the content

with open(p_content_fname, "r") as f:
    p_content_lines = f.readlines() # usually shouldn't be more than one line but idk
    p_content = markdown.markdown("\n".join(p_content_lines))

# get the output filename

cur_datetime = datetime.datetime.utcnow()
cur_timetuple = cur_datetime.utctimetuple()
cur_utc_timestamp = str(calendar.timegm(cur_timetuple))

output_fname = "./posts/" + cur_utc_timestamp + ".html"


# write to the output file

'''
<div id="post">
    <div class="left" id="post-title">
        <h1>Title!</h1>
        <div id="post-date">4-10-22 10:41am</div>
    </div>
    <br/><br/><br/><br/><br/><br/>
    <div id="post-content">
        <p>content!</p>
    </div>
</div>
<hr>
'''

output = f'<div id="post">\n\t<div class="left" id="post-title">\n\t\t<h1>{p_title}</h1>\n\t\t<div id="post-date">{p_date}</div>\n\t</div>\n\t<br/><br/><br/><br/><br/><br/>\n\t<div id="post-content">\n\t\t<p>{p_content}</p>\n\t</div>\n</div>\n\n<hr>'

    
with open(output_fname, "w") as f:
    f.write(output)

# halt!