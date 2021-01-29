
package basic;

public class Literals {
    public static void main(String[] args) {
        int a = 1;
        int c = 5
        double b = 1.9;

        int c = 0x0011;//hex hexadecimal
        System.out.println(c);
        int d = 0b0011;//binary
        System.out.println(d);

        // RGB 0-255 255 255 255=white 000=black
        // FF FF FF=255

        System.out.println(Integer.MAX_VALUE);

        Long e = 2147483648L;
        System.out.println(e);

        float w = 1.0f;
        System.out.println(w);

        //notes:byte < short< int< long< float< double
        
        double value = 1;
        System.out.println(value);
        int VALUE = (int)1.3;
        System.out.println(VALUE);

    }
}

