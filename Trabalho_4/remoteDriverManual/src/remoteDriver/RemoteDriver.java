package remoteDriver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.StringTokenizer;

import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
 
public class RemoteDriver {
	
	static int port = 4321;
	static String host = "localhost";
	
    public static void main(String[] args) throws IOException {
        	    	
        Socket kkSocket = null;
        PrintWriter out = null;
        BufferedReader in = null;
        FIS fis = FIS.load("remoteDriverManual.fcl", true);
        try {
            kkSocket = new Socket(host, port);
            out = new PrintWriter(kkSocket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(kkSocket.getInputStream()));
        } catch (UnknownHostException e) {
            System.err.println("Don't know about host:"  + host);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to: " + host);
            System.exit(1);
        }
 
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
        String fromServer;
 
        double x, y;
        double angle;
        
        out.println("r");
        while ((fromServer = in.readLine()) != null) {
        	StringTokenizer st = new StringTokenizer(fromServer);
        	x = Double.valueOf(st.nextToken()).doubleValue();
        	y = Double.valueOf(st.nextToken()).doubleValue();
        	angle = Double.valueOf(st.nextToken()).doubleValue();

        	System.out.println("x: " + x + " y: " + y + " angle: " + angle);
        	
        	/////////////////////////////////////////////////////////////////////////////////////

        	fis.setVariable("X", x);
			fis.setVariable("ANGLE", angle);

			fis.evaluate();

			double offset = fis.getVariable("STEER").defuzzify();
			System.out.println("STEER value: " + offset);
			out.println(offset);

			out.println("r");
        }
    	System.out.println("SKIP");
 
        out.close();
        in.close();
        stdIn.close();
        kkSocket.close();
    }
}