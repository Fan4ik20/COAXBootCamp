from moviepy.editor import VideoFileClip

from service.stuff import check_path_exist


class Converter:
    @staticmethod
    def convert_and_save(
            converting_dir: str, converting_name: str,
            newfile_dir: str, newfile_name: str
    ) -> None:
        raise NotImplementedError


class VideoToGiffConverter(Converter):
    @staticmethod
    def convert_and_save(
            converting_dir: str, converting_name: str,
            newfile_dir: str, newfile_name: str
    ) -> None:
        check_path_exist(converting_dir)
        check_path_exist(newfile_dir)

        video_file = VideoFileClip(f'{converting_dir}/{converting_name}')
        video_file.write_gif(f'{newfile_dir}/{newfile_name}')
