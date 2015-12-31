This is Music Player from Youtube.

This project is
when I want to listening music without video streaming and downloading from youtube,

I can just listening with conditions.

1. get the stream data from youtube using by `pafy` package.
2. and play it.


## How to Run

- pip install -r requirements.txt (Recommend with pyvenv-3.5)
- python app.py
- http://localhost:5000

There is not required Class Diagram.
Its model is just

```json
{
  "title": video.title,
  "unique_id": video.videoid,
  "length": video.length,
  "src": video.audiostreams[0].url,
  "cover_image_url": video.bigthumb
}
  ```
