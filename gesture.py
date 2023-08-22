{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aefe58d5-0474-4ebe-af42-71ac74db0317",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "background = None\n",
    "accumulated_weight = 0.5\n",
    "\n",
    "ROI_top = 80\n",
    "ROI_bottom = 250\n",
    "ROI_right = 125\n",
    "ROI_left = 325\n",
    "\n",
    "def cal_avg(frame, accumulated_weight):\n",
    "    global background\n",
    "    if background is None:\n",
    "        background = frame.copy().astype(\"float\")\n",
    "        return None\n",
    "    cv2.accumulateWeighted(frame, background, accumulated_weight)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
