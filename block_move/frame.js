function myfun(){
						var elem1=document.getElementById("content1");
						var elem2=document.getElementById("content2");
						var pos1=0
						var pos2=0
						var id1= setInterval(frame1,5);
						var id2= setInterval(frame2,5);
			function frame1(){
						if(pos1==350){
								clearInterval(id1);
							}
							else{ pos1++;
									elem1.style.top = pos1+'px';
									elem1.style.left= pos1+'px';}
			}
			function frame2(){
						if(pos2==350){
								clearInterval(id2);
							}
							else{ pos2++;
									elem2.style.top = pos2+'px';
									elem2.style.right=pos2+'px';}
			}
			
			}