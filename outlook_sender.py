import subprocess


def create_outlook_draft(html_content):

    escaped_html = html_content.replace('"', '\\"')

    script = f'''
    tell application "Microsoft Outlook"
        set newMessage to make new outgoing message with properties {{subject:"Leadership Update"}}
        set content of newMessage to "{escaped_html}"
        open newMessage
    end tell
    '''

    subprocess.run(
        ["osascript", "-e", script]
    )