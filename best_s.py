import cv2
import numpy as np
import json  

table_tennis_table = cv2.imread("resize2.jpg")


cv2.namedWindow("Table Tennis Table")

markers = []


with open("coordinates.json", "r") as file:
    sample_coordinates = json.load(file)

def get_user_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        opponent_bat_position = (x, y)



        closest_distance = float("inf")
        best_spot = None
        for point, coordinates in sample_coordinates.items():
            distance = ((opponent_bat_position[0] - coordinates["user_click"][0]) ** 2 +
                        (opponent_bat_position[1] - coordinates["user_click"][1]) ** 2) ** 0.5
            if distance < closest_distance:
                closest_distance = distance
                best_spot = coordinates["best_spot"]


        for marker in markers:
            cv2.circle(table_tennis_table, marker, 10, (255, 255, 255), -1)
        markers.clear()


        if best_spot is not None:
            cv2.circle(table_tennis_table, best_spot, 10, (0, 0, 255), -1)
            markers.append(best_spot)


        cv2.circle(table_tennis_table, opponent_bat_position, 10, (255, 0, 0), -1)
        markers.append(opponent_bat_position)


        print("Opponent Bat Position:", opponent_bat_position)
        print("Best Spot Coordinates:", best_spot)


        cv2.imshow("Table Tennis Table", table_tennis_table)


cv2.setMouseCallback("Table Tennis Table", get_user_coordinates)
cv2.imshow("Table Tennis Table", table_tennis_table)


cv2.waitKey(0)
cv2.destroyAllWindows()
