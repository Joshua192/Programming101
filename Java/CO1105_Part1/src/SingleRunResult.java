package co1105.cw1.jo189;
import java.util.Scanner;


public class SingleRunResult {

    private int runNumber;
    private float[] scores = new float[7];
    private float hscore = 0;
    private float lscore = 0;
    private float sum = 0;
    private float averagescore;
    private boolean foundhighestscore = true;
    private String nonformatscores = "";
    private String scoreline = "";

    SingleRunResult(int rn, float[] sc){
        this.runNumber = rn;

        for(int i =0; i<7;i++){
            this.scores[i] = sc[i];
        }
        //getResult();
        //this.scoreline = toString();
        lscore = this.scores[0];
        for (int i = 0; i<7; i++){

            if(this.scores[i]>hscore){
                this.hscore = this.scores[i];
            }
            if(this.scores[i]<lscore){
                this.lscore = this.scores[i];
            }
            sum += this.scores[i];
        }
        sum = (sum - this.hscore - this.lscore);
        averagescore = sum/5;
        this.averagescore = getResult();
    }

    public String toString(){
        nonformatscores = nonformatscores + String.valueOf(this.runNumber) + ":";
        for (int n = 0; n<7; n++){
            if (this.scores[n] == this.hscore){
                nonformatscores = nonformatscores + "    " + String.format("%3.1f",this.scores[n]);
                this.hscore = this.scores[n];
            }
            else if (this.scores[n] == this.lscore){
                nonformatscores = nonformatscores + "    " + String.format("%3.1f",this.scores[n]);
                this.lscore = this.scores[n];
            }
            else {
                nonformatscores = nonformatscores + "    " + String.format("%3.1f",this.scores[n]);
            }
        }
        nonformatscores = nonformatscores +  "  == " + String.format("%3.1f",this.getResult());
        Scanner formatscore = new Scanner(nonformatscores);
        this.scoreline = this.scoreline + String.format("%-5s %7s %10s %10s %10s %10s %10s %10s %3s %s",formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next(),formatscore.next());
        if(this.hscore < 10 && foundhighestscore == true){
            this.scoreline = this.scoreline.replaceFirst("  " + this.hscore + " ", "( " + this.hscore + ")");
            foundhighestscore = false;
        }
        else if(this.hscore == 10 && foundhighestscore == true){
            this.scoreline = this.scoreline.replaceFirst(" " + this.hscore + " ", "(" + this.hscore + ")");
            foundhighestscore = false;
        }
        this.scoreline = this.scoreline.replaceFirst("  " + this.lscore + " ", "( " + this.lscore + ")");

        return this.scoreline;
    }

    public float getResult(){

        this.averagescore = averagescore;
        return this.averagescore;
    }

}