#Core Functionality
from engine.auth import recoganize  # #FacialRecognition - Custom facial authentication
from engine.command import speak  # #SpeechOutput - TTS speaking function
from engine.image_gen import (
    generate_image,
)  # #ImageGeneration - AI-based image creation
from engine.config import ASSISTANT_NAME  # #Config - Assistant's name or settings

#Standard Python Libraries
import sys  # #SystemControl - Access system-specific parameters
import os  # #FileOps - OS-level file and path operations
import multiprocessing  # #ParallelProcessing - Running multiple processes
import subprocess  # #RunPrograms - Launch other applications/scripts
import time  # #TimeControl - Time-based operations (sleep, delay)
import datetime  # #DateTime - Handle date and time formats
import re  # #Regex - Pattern matching and parsing
import struct  # #BinaryData - Work with binary structures
import shlex  # #ShellSafeSplit - Parse command strings safely
import csv  # #CSV - Read/write CSV files
import sqlite3  # #Database - Lightweight SQL database

#Computer Vision & UI
import cv2  # #OpenCV - Camera, face detection, vision
import numpy as np  # #Math - Matrix operations (used with images)
from PIL import Image  # #ImageProcessing - Load/save/edit images
import pyautogui  # #ScreenControl - Mouse/keyboard automation

#Audio & Speech
import pyaudio  # #Microphone - Record audio input
import pyttsx3  # #TTS - Text-to-speech engine
import speech_recognition as sr  # #SpeechToText - Recognize voice input

#Internet & API
import requests  # #HTTP - Send web requests (GET, POST)
import webbrowser  # #OpenWeb - Launch browser tabs
import openai  # #AI - Access OpenAI models (e.g., GPT)
from dotenv import load_dotenv  # #Secrets - Load API keys from .env file

#GUI
import eel  # #WebFrontend - Create desktop GUI with HTML/JS
