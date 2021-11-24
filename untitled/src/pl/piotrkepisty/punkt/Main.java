package pl.piotrkepisty.punkt;




public class Main {

    public static void main(String[] args)
    {
//        NazwanyPunkty a = new NazwanyPunkty(3, 5 , "point1 ");
//        a.show();
//        NazwanyPunkty b = new NazwanyPunkty(5, 7 , "point2 ");
//        b.show();
        Adres niba1 = new Adres("arka", 32, 22, "trotorotort", 22777);
        Adres niba2 = new Adres("erfgwe", 11, 33, "adknaonasd", 22776);

        Adres.przed(niba1, niba2);

    }
}
