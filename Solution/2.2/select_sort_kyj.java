/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone{

	public static void main (String[] args) throws java.lang.Exception{
  
		int [] arr = {5, 2, 4, 6, 1, 3}; //초기 배열
		int minIndex = 0; //배열의 인덱스 값
		int tmp = 0;

		for(int i = 0; i < arr.length; i++){
			minIndex = i;
			for(int j = i + 1; j < arr.length; j++){
				if(arr[minIndex] > arr [j]) // 1.가장 작은 값을 선택해서
					minIndex = j; // 2.그 인덱스를 저장하고
			}
			
			tmp = arr[i];
			arr[i] = arr[minIndex]; //3.선택한 값을 위치로 이동
			arr[minIndex] = tmp;
		}

		for(int i = 0; i < arr.length; i++)
			System.out.print(arr[i] + " "); //출력			
  	}
	
}