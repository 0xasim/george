import os
import youtube_dl as yt

def confirm_directory(dir):
  if not os.path.isdir(dir) : os.mkdir(dir)

def get_subtitles(url, dir):
  vid_opts = {
    'outtmpl': f'{dir}/%(title)s-%(id)s.%(ext)s',
    'subtitlesformat': 'srv1', 
    'skip_download': True,
    'writeautomaticsub': True
  }

  try:
    ydl = yt.YoutubeDL(vid_opts)
    #ydl.cache.remove()
    info_dict = ydl.extract_info(url, download=False)
    ydl.prepare_filename(info_dict)
    ydl.download([url])
    return True

  except Exception:
    return False
