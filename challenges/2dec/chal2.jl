
@time function main()
    open("input.txt") do f
        # line_number
    line = 0  
   
    # read till end of file
    while ! eof(f) 
   
       # read a new / next line for every iteration          
       s = readline(f)         
       line += 1
       println("$line . $s")
    end
   
  end
    
end

