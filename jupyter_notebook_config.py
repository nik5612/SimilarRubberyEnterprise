import os;

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' https://replit.com"
  }
}
c.NotebookApp.notebook_dir = "notebooks"
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$JThY7QkmNFXy2jFg6sw1dg$MezCld/XpfW08eTBporFIA'

