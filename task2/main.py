from converters import VideoToGiffConverter
from service.parsing_files import get_video_and_save


def main():
    pass


if __name__ == '__main__':
    test_url = (
        'https://rr18---sn-3c27sn76.googlevideo.com/videoplayback?expire=16'
        '59412316&ei=_EroYtONBbqXx_'
        'APmrqAyA8&ip=95.181.236.9&id=o-AACb12jGT3rnrXFagIbW__lYoA9h3S6avD'
        'TzfAWDewjd&itag=242&aitags=133%2C160%2'
        'C242%2C278&source=youtube&requiressl=yes&spc=lT-Khk1_OP8wc2tDV6i-'
        'CFgdi3ynB1A&vprv=1&mime=video%2Fw'
        'ebm&ns=F9PeoWlIRpEs63hebI6Kx0IH&gir=yes&clen=26790&dur=2.560&lmt='
        '1577116682939061&keepalive=yes&fe'
        'xp=24001373,24007246&c=WEB&txp=5431432&n=PGVE-aT4r1CDNA&sparams=e'
        'xpire%2Cei%2Cip%2Cid%2Caitags%2C'
        'source%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2'
        'Clmt&sig=AOq0QJ8wRgIhAJi3mQZACw0fZr'
        '7ZBNVo2tLoiEleBWmE0ryK1e0jvhtBAiEA3i30TGLs7DXFyDMYZvF8S_KCxiO9ymf'
        'D4fdehmY2840%3D&rm=sn-4g5eks7z&req_i'
        'd=8af45632da5aa3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-05gox'
        'u-afvl7k&cms_redirect=yes&cmsv='
        'e&mh=21&mip=194.44.201.153&mm=29&mn=sn-3c2'
        '7sn76&ms=rdu&mt=1659390543&mv=m&mvi=18&pl=24&lsparams=ipbypass,mh'
        ',mip,mm,mn,ms,mv,mvi,pl&lsig=A'
        'G3C_xAwRQIhAP08A5Ius1rnye1HQy4J9ysppBxQcaO3plejUqDlyY4kAiBV_Ci40ct'
        'DTWW6FQbJMca2qSxI8Sb1PePn5yiMpGh0Pw%3D%3D'
    )

    video_directory = './data/videos'
    video_name = 'test1.webm'

    gif_directory = './data/gifs'
    gif_filename = 'test1.gif'

    get_video_and_save(test_url, video_directory, video_name)

    VideoToGiffConverter.convert_and_save(
        video_directory, video_name, gif_directory, gif_filename
    )
