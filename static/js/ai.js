var cols = ["col-0","col-1","col-2","col-3","col-4","col-5","col-6"];

var aiPlayer = players[1];

function nextBoards(currentBoard, player) {
    var boards = []
    for (var col=0; col < cols.length; col++) {
        var nextBoard = $.extend(true, [], board);
        if (nextBoard[col].length < 6) {
            nextBoard[col].push(aiPlayer);
            boards.push(nextBoard);
        } else {
            boards.push(null);
        }
    }

    return boards;
}

function aiMove() {
    console.log('NEW TURN');
    var col = minimax(3);

    addTile(cols[col]);

}

function minimax(depth) {
    var scores = [];
    var boards = nextBoards(board, aiPlayer);
    for (var i=0; i < boards.length; i++) {
        if (boards[i] !== null) {
            scores.push(minimaxScore(boards[i], depth, aiPlayer));
        } else {
            scores.push(Number.MIN_VALUE);
        }
        console.log('Column: ' + i + ' Score: ' + scores[i]);
    }

    maxScore = Number.MIN_VALUE;
    maxScoreIndex = 0;

    for (var i=0; i < scores.length; i++) {
        if (scores[i] > maxScore && isLegal(i)) {
            maxScore = scores[i];
            maxScoreIndex = i;
        }
    }

    return maxScoreIndex;

}

function minimaxScore(nextBoard, depth, player) {
    var opponent = (player === players[0]) ? players[1] : players[0];

    if (depth === 0 || true) {
        score = boardScore(nextBoard, opponent);
        return score;
    }


    var scores = [];
    var boards = nextBoards(nextBoard, opponent);
    for (var i=0; i < boards.length; i++) {
        if (boards[i] !== null) {
            scores.push(minimaxScore(boards[i], depth-1, opponent));
        } else {
            scores.push(Number.MIN_VALUE);
        }
    }

    maxScore = Number.MIN_VALUE;

    for (var i=0; i < scores.length; i++) {
        if (scores[i] > maxScore) {
            maxScore = scores[i];
        }
    }
    return maxScore;
}

function boardScore(nextBoard, player) {
    var score = 0;

    var opponent = (player === players[0]) ? players[1] : players[0];

    for (var line=0; line < lines.length; line++) {
        var myChain = 0;
        var theirChain = 0;
        for (var tile=0; tile < lines[line].length; tile++) {
            var col = lines[line][tile][0];
            var row = lines[line][tile][1];

            // subtract 10^n for each n-row chain the opponent has
            // and add 10^n for each n-row chain we have
            if (nextBoard[col][row] === player) {
                myChain++;
                score -= Math.pow(10, theirChain);
                theirChain = 0;
            } else if (board[col][row] === opponent) {
                theirChain++;
                score += Math.pow(10, myChain);
                myChain = 0;
            } else {
                score += Math.pow(10, myChain);
                score -= Math.pow(10, theirChain);
                myChain = 0;
                theirChain = 0;
            }
            if (theirChain === 4) {
                score = Number.MAX_VALUE;
            }
            if (myChain === 4) {
                score = Number.MAX_VALUE;
            }
        }
    }
    return score;
}
