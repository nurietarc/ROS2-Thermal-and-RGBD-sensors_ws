import numpy as np
from colorama import Fore, Style

"""
Nuria Rodríguez Calderón
    This class is responsible for correcting the order of corners detected in chessboard images.
    It ensures that the order of corners from two different images is consistent, which is crucial for accurate homography calculation.
"""

class CornerOrderCorrector:
    @staticmethod
    def correct_corners(reference_corners, corners_to_reorder):
        """
        Reorder corners_to_reorder to match the reference_corners if needed.
        
        Parameters:
        - reference_corners: Array of reference corners to which the other corners should be aligned.
        - corners_to_reorder: Array of corners that may need reordering.
        
        Returns:
        - Reordered corners_to_reorder, if needed.
        """
        if len(corners_to_reorder) > 0:
            # Calculate directions for reference_corners and corners_to_reorder
            reference_directions = np.diff(reference_corners, axis=0)
            reorder_directions = np.diff(corners_to_reorder, axis=0)

            # Compare directions to check if they are consistent
            if not np.allclose(reference_directions, reorder_directions, atol=1e-5):
                print(Fore.BLUE + "\nCorners were not detected in the same order. Reordering corners..." + Style.RESET_ALL)
                corners_to_reorder = corners_to_reorder[::-1]  # Reverse the order of corners
        
        return corners_to_reorder