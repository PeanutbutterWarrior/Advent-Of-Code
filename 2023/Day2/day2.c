#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_GAMES 100
#define MAX_LINE 200

#define min(a, b) (a) < (b) ? (a) : (b)
#define max(a, b) (a) > (b) ? (a) : (b)

typedef struct pull {
    int red;
    int green;
    int blue;
} Pull;

typedef struct game {
    int numPulls;
    Pull * pulls;
} Game;

 
void main() {
    FILE * file = fopen("input.txt", "r");
    Game games[NUM_GAMES];
    char linebuf[MAX_LINE];
    int gameNum = 0;

    while (fgets(linebuf, MAX_LINE, file) != NULL) {
        int numPulls = 1;
        for (char * c = linebuf; *c != 0; c++)
            if (*c == ';')
                numPulls++;
        games[gameNum].pulls = calloc(numPulls, sizeof(Pull));
        games[gameNum].numPulls = numPulls;

        char * linescan = linebuf;
        while (*linescan++ != ':') ;

        int pullNum = 0;
        while (*linescan != 0) {
            if (*linescan == ';')
                pullNum++;
            else if ('0' < *linescan && *linescan <= '9') {
                int num = strtol(linescan, &linescan, 10);
                linescan++;
                switch (*linescan) {
                    case 'r':
                        games[gameNum].pulls[pullNum].red = num;
                        break;
                    case 'g':
                        games[gameNum].pulls[pullNum].green = num;
                        break;
                    case 'b':
                        games[gameNum].pulls[pullNum].blue = num;
                        break;
                    default:
                        printf("Weird color line %d, pull %d, index %d\n", gameNum + 1, pullNum + 1, linescan - linebuf);
                }
            }
            linescan++;
        }
        gameNum++;
    }


    int part1Sol = 0;
    for (int i=0; i < NUM_GAMES; i++) {
        Game currentGame = games[i];
        int isPossible = 1;
        for (int j=0; j < currentGame.numPulls; j++) {
            Pull currentPull = currentGame.pulls[j];
            if (currentPull.red > 12 || currentPull.green > 13 || currentPull.blue > 14) {
                isPossible = 0;
                break;
            }
        }
        if (isPossible)
            part1Sol += i + 1;
    }
    printf("Part 1 solution: %d\n", part1Sol);

    long long part2Sol = 0;
    for (int i=0; i < NUM_GAMES; i++) {
        Game currentGame = games[i];
        int minr = 0;
        int ming = 0;
        int minb = 0;
        for (int j=0; j < currentGame.numPulls; j++) {
            Pull currentPull = currentGame.pulls[j];
            minr = max(minr, currentPull.red);
            ming = max(ming, currentPull.green);
            minb = max(minb, currentPull.blue);
        }
        long long power = minr * ming * minb;
        part2Sol += power;
    }
    printf("Part 2 solution: %d\n", part2Sol);
}