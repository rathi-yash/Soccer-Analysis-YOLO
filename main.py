from utils import read_video, save_video
from trackers import Tracker
import cv2
from team_assignment import TeamAssignment
from player_ball_assigner import PlayerBallAssigner


def main():
    # Read video
    video_frames = read_video('videos/video1.mp4')

    # Initialise Tracker
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    # Interpolate Ball Positions
    tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])

    # Save cropped image of a player
    # for track_id, player in tracks["players"][0].items():
    #     bounding_box = player["bounding_box"]
    #     frame = video_frames[0]
    #
    #     # crop bounding_box from the frame
    #     cropped_img = frame[int(bounding_box[1]):int(bounding_box[3]), int(bounding_box[0]):int(bounding_box[2])]
    #
    #     # Save the cropped image
    #     cv2.imwrite(f'videos/cropped_img.jpg', cropped_img)

    # Assign Player Teams
    team_assignment = TeamAssignment()
    team_assignment.assign_team_color(video_frames[0], tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assignment.get_player_team(video_frames[frame_num],
                                                   track["bbox"],
                                                   player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks["players"][frame_num][player_id]['team_color'] = team_assignment.team_colors[team]

    # Assign ball Acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])

    # Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save Video
    save_video(output_video_frames, 'videos/video1_output.avi')


if __name__ == '__main__':
    main()
