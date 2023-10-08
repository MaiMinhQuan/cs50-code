#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            int ave = (int) ((red + green + blue) / 3.0 + 0.5);
            image[i][j].rgbtRed = ave;
            image[i][j].rgbtGreen = ave;
            image[i][j].rgbtBlue = ave;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int red = image[i][j].rgbtRed;
    int green = image[i][j].rgbtGreen;
    int blue = image[i][j].rgbtBlue;

    image[i][j].rgbtRed = fmin (255, (int)(0.393 * red + 0.769 * green + 0.189 * blue));
    image[i][j].rgbtGreen = fmin (255, (int)(0.349 * red + 0.686 * green + 0.168 * blue));
    image[i][j].rgbtBlue = fmin(255, (int)(0.272 * red + 0.534 * green + 0.131 * blue));
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - 1 -j];
            image[i][width - 1 - j] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < heught; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0'
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    
                }
            }
        }
    }
    return;
}
