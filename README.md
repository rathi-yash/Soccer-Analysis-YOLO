# Soccer-Analysis-YOLO
## Project Overview

This project leverages advanced computer vision and machine learning techniques to analyze football (soccer) match videos. Our key objectives include:

### Object Detection and Tracking
- Utilize YOLO (You Only Look Once) for real-time detection and tracking of players, referees, and footballs.
- Fine-tune the YOLO model to enhance detection accuracy.

### Team Assignment
- Implement K-means clustering for pixel segmentation to identify team colors.
- Assign players to their respective teams based on jersey colors.

### Ball Possession Analysis
- Calculate and visualize each team's ball possession percentage throughout the match.

### Movement Analysis
- Apply optical flow techniques to measure camera movement between frames.
- Implement perspective transformation to accurately represent scene depth.
- Convert player movement from pixels to real-world distances (meters).

### Performance Metrics
- Calculate player speed and total distance covered during the match.

This comprehensive project combines various computer vision concepts to solve real-world sports analysis problems, making it suitable for both beginners and experienced machine learning engineers.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rathi-yash/Soccer-Analysis-YOLO.git
   cd Soccer-Analysis-YOLO
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

The following libraries are used in this project:

- ultralytics
- numpy
- opencv-python
- roboflow
- pandas
- pickle
- supervision
- shutil
- scikit-learn

## Usage

1. **Data Preparation:**

   - Place your video footage of the football match in the `input` directory.

2. **Running the Analysis:**

   - Execute the main script `python main.py` to initiate the analysis process.
   - The analysis encompasses the following key steps:
     - Object tracking using YOLO for players, referees, and the football.
     - Estimating camera movements to understand viewpoint changes.
     - Calculating player speed, distance traveled, and determining ball possession.
     - Visualizing analysis results on the video frames.

3. **Output:**
   - The annotated and analyzed video will be saved in the `output_videos` directory for review.

## Code Structure

- **`utils.py`**: Contains utility functions for video I/O operations.
- **`trackers.py`**: Implements the YOLO-based object tracker and interpolation techniques.
- **`team_assigner.py`**: Assigns teams to players based on their visual appearance.
- **`player_ball_assigner.py`**: Determines ball possession among players during the match.
- **`camera_movement_estimator.py`**: Estimates camera movements to analyze perspective changes.
- **`view_transformer.py`**: Transforms object positions based on the camera view for accurate analysis.
- **`speed_and_distance_estimator.py`**: Calculates player speeds and distances traveled for performance evaluation.

## Contributing

Contributions, feedback, and suggestions are highly encouraged! Please feel free to open an issue or submit a pull request with any improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the YOLOv5 team and the contributors of the libraries used in this project for their valuable contributions to the field of object detection and analysis in computer vision.