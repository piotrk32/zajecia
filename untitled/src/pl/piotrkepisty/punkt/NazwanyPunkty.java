package pl.piotrkepisty.punkt;

public class NazwanyPunkty extends Punkt
{
    private String name;

    public NazwanyPunkty(int x, int y, String name)
    {
        super(x, y);
        this.name = name;
    }

    public void show()
    {
        System.out.println(name + "<" + " " + getX() + "," + getY() + " " + ">");
    }

}
