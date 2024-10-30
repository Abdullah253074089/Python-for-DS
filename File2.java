import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class StudentExamAnalyzer {
    
    public static void main(String[] args) {
        try {
            // Create a File object for the input file
            File inputFile = new File("students.txt");
            
            // Create a Scanner object to read the input file
            Scanner reader = new Scanner(inputFile);
            
            // Variables to track total students, highest, lowest scores, and averages
            int totalStudents = 0;
            int highestTotal = Integer.MIN_VALUE;
            int lowestTotal = Integer.MAX_VALUE;
            String highestScorer = "";
            String lowestScorer = "";
            
            int mathTotal = 0, scienceTotal = 0, englishTotal = 0;
            
            // Create a FileWriter to write output to results.txt
            FileWriter outputFile = new FileWriter("results.txt");
            
            // Process each student in the input file
            while (reader.hasNextLine()) {
                String line = reader.nextLine();
                
                // Split the line by commas
                String[] studentData = line.split(", ");
                
                // Extract student details
                String name = studentData[0];
                int rollNumber = Integer.parseInt(studentData[1]);
                int mathMarks = Integer.parseInt(studentData[2]);
                int scienceMarks = Integer.parseInt(studentData[3]);
                int englishMarks = Integer.parseInt(studentData[4]);
                
                // Calculate the total marks
                int totalMarks = mathMarks + scienceMarks + englishMarks;
                
                // Update subject totals for averages
                mathTotal += mathMarks;
                scienceTotal += scienceMarks;
                englishTotal += englishMarks;
                
                // Track highest and lowest scorers
                if (totalMarks > highestTotal) {
                    highestTotal = totalMarks;
                    highestScorer = name;
                }
                
                if (totalMarks < lowestTotal) {
                    lowestTotal = totalMarks;
                    lowestScorer = name;
                }
                
                // Output the student total to the results file
                outputFile.write(name + " (Roll No: " + rollNumber + ") - Total Marks: " + totalMarks + "\n");
                
                totalStudents++;
            }
            
            // Calculate and write averages to the results file
            outputFile.write("\nSubject Averages:\n");
            outputFile.write("Math: " + (mathTotal / totalStudents) + "\n");
            outputFile.write("Science: " + (scienceTotal / totalStudents) + "\n");
            outputFile.write("English: " + (englishTotal / totalStudents) + "\n");
            
            // Write the highest and lowest scorers to the results file
            outputFile.write("\nHighest Scorer: " + highestScorer + " with " + highestTotal + " marks\n");
            outputFile.write("Lowest Scorer: " + lowestScorer + " with " + lowestTotal + " marks\n");
            
            // Close the file objects
            reader.close();
            outputFile.close();
            
            System.out.println("Analysis complete. Results saved to results.txt.");
            
        } catch (IOException e) {
            // Handle file reading/writing errors
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
