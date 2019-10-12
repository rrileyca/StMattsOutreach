currentDir=$(pwd)

baseDir="$HOME/Desktop/LessonMaterial"
week4Dir="$baseDir/Week_4"
week5Dir="$baseDir/Week_5"
week6Dir="$baseDir/Week_6"


# Base setup
if [ ! -d "$baseDir" ]; then
    mkdir -p "$baseDir"
fi


# Week 4
if [ ! -d "$week4Dir" ]; then
    mkdir -p "$week4Dir"
fi

wget -O "$week4Dir/Week4Lesson.py" https://git.io/fjUTK




# Week 5
if [ ! -d "$week5Dir" ]; then
    mkdir -p "$week5Dir"
fi

wget -O "$week5Dir/Week5Lesson.py" https://git.io/fjUTr
wget -O "$week5Dir/Week5Challenges.py" https://git.io/fjqeg



# Week 6
if [ ! -d "$week6Dir" ]; then
    mkdir -p "$week6Dir"
fi

wget -O "$week6Dir/Week6Lesson.py" https://git.io/fjkyz
wget -O "$week6Dir/Week6Challenges.py" https://git.io/fjky2



