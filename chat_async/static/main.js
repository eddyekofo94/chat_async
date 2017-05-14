$(document).ready(function () {
      var socket = io.connect('http://localhost:6543', { reconnect: true });
      if(socket.connected){
          console.log("Server connected");
      }else {
          console.log('Server not connected');
      }

      // socket
      var char = $('chart').get(0);

      socket.on('connect', function () {
          console.log(socket.connected);
          console.log('user connected');
          if (chart.getContext) {
            render();
            window.onresize = render;

         }
        send();
      });
      console.log('line 18', socket.connected);
      socket.on('pong_from_server', function () {
        console.log ("event", socket.connected);
        socket.emit(data);
        console.log('ponged');
        var latency = new Date - last;
        $('#latency').text(latency + 'ms');
        if (time)
            time.append(+new Date, latency);
        setTimeout(send, 100);

      });

    socket.on('disconnect', function() {
        if (smoothie)
            smoothie.stop();
        $('#transport').text('(disconnected)');
    });
    var last;
    function send() {
        last = new Date;
        socket.emit('ping_from_client');
        $('#transport').text(socket.io.engine.transport.name);
    }
    // chart
    var smoothie;
    var time;
    function render() {
        if (smoothie)
            smoothie.stop();
        chart.width = document.body.clientWidth;
        smoothie = new SmoothieChart();
        smoothie.streamTo(chart, 1000);
        time = new TimeSeries();
        smoothie.addTimeSeries(time, {
            strokeStyle: 'rgb(255, 0, 0)',
            fillStyle: 'rgba(255, 0, 0, 0.4)',
            lineWidth: 2,
        });
    }
    });
