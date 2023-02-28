Problem B

Lots of runners use personal Global Positioning System (GPS) receivers to track how many miles they run. No GPS is perfect, though: it only records its position periodically rather than continuously, so it can miss parts of the true running path. For this problem we’ll consider a GPS that works in the following way when tracking a run:

    At the beginning of the run, the GPS first records the runner’s starting position at time 0.

    It then records the position every t units of time.

    It always records the position at the end of the run, even if the total running time is not a multiple of t.

The GPS assumes that the runner goes in a straight line between each consecutive pair of recorded positions. Because of this, a GPS can underestimate the total distance run.

For example, suppose someone runs in straight lines and at constant speed between the positions on the left side of Table 1. The time they reach each position is shown next to the position. They stopped running at time 11. If the GPS records a position every 2 units of time, its readings would be the records on the right side of Table 1.


Table 1: Actual Running Path on the left, GPS readings on the right.

The total distance run is approximately 14.313 units, while the GPS measures the distance as approximately 11.650281 units. The difference between the actual and GPS distance is approximately 2.6634 units, or approximately 18.6075% of the total run distance.

Given a sequence of positions and times for a running path, as well as the GPS recording time interval t, calculate the percentage of the total run distance that is lost by the GPS. Your computations should assume that the runner goes at a constant speed in a straight line between consecutive positions.

Input

The input consists of a single test case. The first line contains two integers(2<=n<=100) and t (1<=t<=100), where n is the total number of positions on the running path, and t is the recording time interval of the GPS (in seconds).

The next lines contain three integers per line. The i-th line has three integers xi,yi (10^-6<=xi,yi<=10^6), and ti(0<=ti<=10^6), giving the coordinates of the i-th position on the running path and the time (in seconds) that position is reached. The values of ti’s are strictly increasing. The first and last positions are the start and end of the run. Thus, t1 is always zero.

It is guaranteed that the total run distance is greater than zero.

Output

Output the percentage of the actual run distance that is lost by the GPS. The answer is considered correct if it is within 10^-5 of the correct answer.

Sample Input 1 	

6 2
0 0 0
0 3 3
-2 5 5
0 7 7
2 5 9
0 3 11

	
Sample Output 1

18.60752550117103
