\documentclass[a4paper,12pt]{article}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{fancyhdr}
\pagestyle{fancy}

% Set up document title and author
\title{Sentiment-Driven Portfolio Optimizer}
\author{Maaz Khalid}
\date{\today}

\begin{document}

\maketitle

\section*{Overview}
The \textbf{Sentiment-Driven Portfolio Optimizer} is an automated system that uses sentiment analysis on financial news headlines to adjust portfolio weights across different sectors. The model classifies news headlines into one of five sectors (such as Technology, Energy, Healthcare, Finance, and Geopolitical), performs sentiment analysis, and adjusts the weights of the portfolio based on the sentiment of each sector. This approach aims to help investors optimize their portfolio based on market sentiment.

The optimizer dynamically reallocates weights in the portfolio based on the sentiment (positive, neutral, or negative) observed for each sector, which could potentially improve returns and reduce risks.

\section*{Project Structure}

\subsection*{main.py}
This is the central script that integrates all the components of the optimizer. It:
\begin{itemize}
    \item Fetches news articles from the past 10 days based on a list of predefined keywords.
    \item Classifies news headlines into one of five sectors: \textbf{Technology}, \textbf{Energy}, \textbf{Healthcare}, \textbf{Finance}, and \textbf{Geopolitical}.
    \item Analyzes the sentiment of the classified news for each sector and calculates sentiment scores.
    \item Adjusts the portfolio weights dynamically based on the sentiment scores for each sector.
\end{itemize}

\subsubsection*{Key Functions:}
\begin{itemize}
    \item \textbf{Fetching News:} It fetches headlines from a news API (e.g., NewsAPI) for a given period.
    \item \textbf{Classifying Sectors:} Headlines are classified based on predefined sector-specific keywords using the \texttt{classify\_sector} function.
    \item \textbf{Sentiment Analysis:} The sentiment of the classified headlines is analyzed using a pre-trained model in the \texttt{analyze\_combined\_sentiment} function.
    \item \textbf{Adjusting Portfolio:} Portfolio weights are adjusted based on the sentiment analysis using \texttt{adjust\_portfolio\_weights}.
\end{itemize}

\subsection*{fetch\_news.py}
This module contains functions to fetch news headlines for specific dates and keywords.

\subsubsection*{Key Functions:}
\begin{itemize}
    \item \texttt{fetch\_broader\_market\_news(API\_KEY, keywords, from\_date, to\_date):} This function makes an API call to fetch market news articles between the specified date range (\texttt{from\_date} to \texttt{to\_date}). The articles are filtered using a list of keywords related to economic and financial factors.
    \item \texttt{get\_past\_n\_days(n):} This function calculates the dates for the last \texttt{n} days (in this case, 10 days) and returns them in the format required for the \texttt{fetch\_broader\_market\_news} function.
\end{itemize}

\subsection*{classify\_sector.py}
This file contains the logic for classifying news headlines into sectors. Each sector is associated with a list of keywords.

\subsubsection*{Key Function:}
\begin{itemize}
    \item \texttt{classify\_sector(headlines):} This function takes in a list of news headlines, checks for the presence of sector-related keywords, and classifies the headlines into appropriate sectors (Technology, Energy, Healthcare, Finance, and Geopolitical). It returns a dictionary mapping each sector to its respective headlines.
\end{itemize}

\subsection*{sentiment\_analysis.py}
This module handles the sentiment analysis of the classified headlines. The function used here analyzes the sentiment of each headline and assigns sentiment scores.

\subsubsection*{Key Function:}
\begin{itemize}
    \item \texttt{analyze\_combined\_sentiment(data):} This function takes in the classified headlines (from \texttt{classify\_sector}) and analyzes the sentiment using a sentiment analysis model (e.g., Hugging Face’s BERT-based models). It returns a sentiment score along with the probability of positive, neutral, and negative sentiment for each sector on a specific day.
\end{itemize}

\subsection*{adjust\_portfolio.py}
The logic in this module adjusts the portfolio weights based on sentiment analysis results. If a sector shows positive sentiment, its weight may increase, and if it shows negative sentiment, its weight may decrease.

\subsubsection*{Key Function:}
\begin{itemize}
    \item \texttt{adjust\_portfolio\_weights(sentiment\_results, portfolio):} This function takes the sentiment analysis results and the initial portfolio weights. It adjusts the portfolio weights based on the sentiment of each sector. The higher the positive sentiment, the more weight is assigned to the corresponding sector, while negative sentiment results in a reduced weight. The portfolio is adjusted dynamically for each day’s sentiment.
\end{itemize}

\section*{Workflow Overview}

\begin{enumerate}
    \item \textbf{Fetching News:} The system begins by fetching the latest news for the past \texttt{n} days using the \texttt{get\_past\_n\_days} function. It then uses the \texttt{fetch\_broader\_market\_news} function to collect the headlines for each day.
    \item \textbf{Classifying Headlines:} Once the headlines are fetched, the \texttt{classify\_sector} function categorizes them into their respective sectors based on the presence of sector-specific keywords.
    \item \textbf{Sentiment Analysis:} The \texttt{analyze\_combined\_sentiment} function is used to process the classified headlines. It calculates a sentiment score for each sector, which indicates whether the sentiment is positive, neutral, or negative for the given sector on that day.
    \item \textbf{Adjusting Portfolio Weights:} Finally, the \texttt{adjust\_portfolio\_weights} function takes the sentiment results and adjusts the portfolio weights accordingly. Positive sentiment increases the weight of a sector, while negative sentiment decreases it.
\end{enumerate}

\section*{Sample Output}

The output of the \texttt{main.py} script includes:
\begin{itemize}
    \item \textbf{Sentiment Results:} For each day, sentiment scores are computed for all sectors based on the analyzed headlines.
\end{itemize}

Example:
\begin{verbatim}
Sentiment Results:
{
    '2025-01-06': {'Energy': {'sentiment_score': 0.1, 'positive_prob': 0.6, 'neutral_prob': 0.3, 'negative_prob': 0.1}},
    '2025-01-07': {'Finance': {'sentiment_score': -0.5, 'positive_prob': 0.2, 'neutral_prob': 0.5, 'negative_prob': 0.3}}
}
\end{verbatim}

\begin{itemize}
    \item \textbf{Adjusted Portfolio Weights:} Based on the sentiment analysis, the portfolio weights are adjusted to allocate more funds to sectors with positive sentiment and reduce exposure to sectors with negative sentiment.
\end{itemize}

Example:
\begin{verbatim}
Adjusted Portfolio Weights:
  Technology: 0.18
  Energy: 0.16
  Healthcare: 0.26
  Finance: 0.16
  Geopolitical: 0.24
\end{verbatim}

\section*{License}
This project is licensed under the MIT License - see the \texttt{LICENSE} file for details.

\section*{Acknowledgements}
\begin{itemize}
    \item \textbf{NewsAPI}: For providing access to the financial news articles.
    \item \textbf{Hugging Face}: For the pre-trained sentiment analysis models.
\end{itemize}

\end{document}
