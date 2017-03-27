/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone{

	public static void main (String[] args) throws java.lang.Exception{
  
		int [] arr = {5, 2, 4, 6, 1, 3}; //
    		
    		for(int i = 1; i < arr.length; i++) {
			int standard = arr[i];  //sorting 시작값
      			int index = i - 1;   // 좌측두번째부터
			
			while(index >= 0 && arr[index] > standard ){ //오름차순
        			arr[index + 1] = arr[index];   // 이동				
        			index--;
			}
      
			arr[index + 1] = standard; 
		}
		
		for(int i = 0; i < arr.length; i++)
			System.out.print(arr[i] + " "); //출력	
	}

	
}
