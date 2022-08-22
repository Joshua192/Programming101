package co1105.cw1.jo189;
public class Skier {
    private String name;
    private SingleRunResult run1;
    private SingleRunResult run2;
    private String run1score;
    private String run2score;
    private Float run1result;
    private Float run2result;
    private Float bestscore;
    private String fullscore = "";

    Skier(String n, SingleRunResult r1, SingleRunResult r2){
        this.name = n;
        this.run1 = r1;
        this.run2 = r2;
        this.run1score = this.run1.toString();
        this.run2score = this.run2.toString();
        this.run1result = this.run1.getResult();
        this.run2result = this.run2.getResult();
        //this.fullscore = toString();
        //this.bestscore = getResult();

    }

    public String toString(){
        this.fullscore = this.name + "  :   " + String.format("%3.1f",getResult()) + "\n";
        if(getResult() == this.run1result){
            this.fullscore = this.fullscore + "   " + this.run1score + " " + "\n";
            this.fullscore = this.fullscore + String.format("%-3s", "[") + this.run2score + String.format("%3s %n","]");
        }
        else if(getResult() == this.run2result){
            this.fullscore = this.fullscore + String.format("%-3s", "[") + this.run1score + String.format("%3s %n","]");
            this.fullscore = this.fullscore + "   " + this.run2score + " " + "\n";

        }
        return this.fullscore;
    }

    public float getResult(){
        this.bestscore = this.run1result;
        if(this.bestscore < this.run2result){
            this.bestscore = this.run2result;
        }
        return this.bestscore;
    }

    public String getName(){
        this.name = name;
        return this.name;
    }


}