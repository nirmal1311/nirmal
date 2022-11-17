import java.io.*;
import java.net.InetAddress;

public class subnet {

    public static void main(String[] args) throws IOException {

        System.out.println("ENTER IP:");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ip = br.readLine();
        String checkclass = ip.substring(0, 4);

        int cc = Integer.parseInt(checkclass);
        String mask = null;
        if (cc > 0 && cc < 224) {
            if (cc < 127) {
                mask = "255.0.0.0";
            }
            if (cc > 128 && cc < 192) {
                mask = "255.255.0.0";
            }
            if (cc >= 192) {
                mask = "255.255.255.0";
            }
        }
        System.out.println("MASK:\n" + mask);
    }

}
