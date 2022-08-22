package co1105.cw1.jo189;
public class ScoreBoard {

    private Skier[] skiers;
    private Float winnerscore;
    private Skier winningskier;
    private String scoreboard = "";

    ScoreBoard(Skier[] sk){
        this.skiers = sk;
        this.winningskier = getWinner();

    }

    public Skier getWinner(){
        this.winnerscore = this.skiers[0].getResult();
        this.winningskier = this.skiers[0];
        for(int i = 0; i<this.skiers.length;i++){
            if(this.skiers[i].getResult() > this.winnerscore){
                this.winnerscore = this.skiers[i].getResult();
                this.winningskier = this.skiers[i];
            }
        }

        return this.winningskier;
    }

    public String toString(){
        for(int index = 0; index < this.skiers.length;index++){
            this.scoreboard = this.scoreboard + this.skiers[index].toString();
        }
        return this.scoreboard;

    }
}
