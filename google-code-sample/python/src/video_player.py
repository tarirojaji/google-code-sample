"""A video player class."""
import random
from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self.isPlaying = True
        self.video_now = None

        # self.playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)

        for video in all_videos:
            print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # video = self._video_library.get_video(video_id)
        # if video:
        #     print(f'Playing video: {video.title}')
        #     self._current_video = video
        # else:
        #     print("Cannot play video: Video does not exist")





        # video = self._video_library.get_video(video_id)
        # if not video:
        #     print("Cannot play video: Video does not exist")
        #     return

        # if self._current_video:
        #     print(f'Stopping video: {video.title}')
        
        # self._current_video = video
        # print(f'Playing video: {video.title}')




        valid_video = self._video_library.get_video(video_id)
        if not valid_video:
            print("Cannot play video: Video does not exist")
            return
        if not self._current_video:
            video = self._video_library.get_video(video_id)
            print(f'Playing video: {video.title}')
            self._current_video = self._video_library.get_video(video_id)
        elif self._current_video:
            print(f'Stopping video: {self._current_video.title}')
            video = self._video_library.get_video(video_id)
            print(f'Playing video: {video.title}')


    def stop_video(self):
        """Stops the current video."""

        if self._current_video:
            print(f'Stopping video: {self._current_video.title}')
            self._current_video = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        random_video = random.choice(all_videos)

        # print(f'Playing video: {random_video.title}')

        if not self._current_video:
            print(f'Playing video: {random_video.title}')
            self._current_video = self._video_library.get_video(random_video.video_id)
        elif self._current_video:
            print(f'Stopping video: {self._current_video.title}')
            print(f'Playing video: {random_video.title}')



    def pause_video(self):
        """Pauses the current video."""
        # if self._current_video and self.isPlaying:
        #     print(f'Pausing video: {self._current_video.title}')
        #     self.isPlaying = False
        # else:
        #     print(f'Video already paused:: {self._current_video.title}')

        if self._current_video:
            if self.isPlaying:
                print(f"Pausing video: {self._current_video.title}")
                self.isPlaying = False
            else:
                print(f"Video already paused:: {self._current_video.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video:
            if self.isPlaying:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self._current_video.title}")
                self.isPlaying = True
        else:
            print("Cannot continue video: No video is currently playing")

        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video:
            if self.isPlaying:
                print(f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{' '.join(self._current_video.tags)}]")
            else:
                print(f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{' '.join(self._current_video.tags)}] - PAUSED")
        else:
            print("No video is currently playing")

        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
